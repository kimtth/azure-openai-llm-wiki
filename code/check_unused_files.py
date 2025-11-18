# Check for unused files in the files directory and move them to bak directory
# This script scans all markdown files and checks if files in 'files' directory are referenced

import os
import re
import shutil

def get_all_markdown_files(root_dir):
    """Get all markdown files in the repository."""
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip archive and bak directories
        dirs[:] = [d for d in dirs if d not in ['archive', 'bak', '.git', 'node_modules']]
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def extract_file_references(md_content):
    """Extract all file references from markdown content."""
    references = set()
    
    # Pattern 1: Markdown image syntax ![alt](path)
    img_pattern = r'!\[.*?\]\((.*?)\)'
    references.update(re.findall(img_pattern, md_content))
    
    # Pattern 2: Markdown link syntax [text](path)
    link_pattern = r'\[.*?\]\((.*?)\)'
    references.update(re.findall(link_pattern, md_content))
    
    # Pattern 3: HTML img tags <img src="path">
    html_img_pattern = r'<img\s+[^>]*src=["\']([^"\']+)["\']'
    references.update(re.findall(html_img_pattern, md_content))
    
    # Pattern 4: Direct file references in text (e.g., files/something.pdf)
    file_ref_pattern = r'(?:files|\.\.\/files)\/[^\s\)"\'>]+'
    references.update(re.findall(file_ref_pattern, md_content))
    
    return references

def normalize_path(ref_path):
    """Normalize path to extract just the filename from files directory."""
    # Remove URL fragments and query strings
    ref_path = ref_path.split('#')[0].split('?')[0]
    
    # Extract filename if path contains 'files'
    if 'files' in ref_path:
        parts = ref_path.split('files/')
        if len(parts) > 1:
            return parts[-1].strip()
    
    return None

def scan_markdown_for_references(root_dir):
    """Scan all markdown files and collect referenced files."""
    md_files = get_all_markdown_files(root_dir)
    all_references = set()
    
    print(f"Scanning {len(md_files)} markdown files...")
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                refs = extract_file_references(content)
                
                # Normalize paths
                for ref in refs:
                    normalized = normalize_path(ref)
                    if normalized:
                        all_references.add(normalized)
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    return all_references

def get_files_in_directory(files_dir, include_subdirs=False, subdir_name=None):
    """Get all files in the files directory.
    
    Args:
        files_dir: Base directory to scan
        include_subdirs: If True, scan subdirectories
        subdir_name: Specific subdirectory to scan (e.g., 'archive')
    """
    files_list = []
    
    if not os.path.exists(files_dir):
        print(f"Directory {files_dir} does not exist!")
        return files_list
    
    if subdir_name:
        # Scan specific subdirectory
        subdir_path = os.path.join(files_dir, subdir_name)
        if os.path.exists(subdir_path):
            for item in os.listdir(subdir_path):
                item_path = os.path.join(subdir_path, item)
                if os.path.isfile(item_path):
                    files_list.append(os.path.join(subdir_name, item))
    else:
        # Scan main directory only
        for item in os.listdir(files_dir):
            item_path = os.path.join(files_dir, item)
            if os.path.isfile(item_path):
                files_list.append(item)
    
    return files_list

def move_unused_files(root_dir, files_dir, dry_run=True, check_archive=False):
    """Move unused files to bak directory."""
    # Get all references from markdown files
    referenced_files = scan_markdown_for_references(root_dir)
    print(f"\nFound {len(referenced_files)} unique file references in markdown files.")
    
    # Get all files in files directory or archive subdirectory
    if check_archive:
        all_files = get_files_in_directory(files_dir, subdir_name='archive')
        target_dir = os.path.join(files_dir, 'archive')
        print(f"Found {len(all_files)} files in {target_dir}")
    else:
        all_files = get_files_in_directory(files_dir)
        target_dir = files_dir
        print(f"Found {len(all_files)} files in {target_dir}")
    
    # Find unused files
    unused_files = []
    for file in all_files:
        # For archive files, need to check with archive/ prefix
        file_to_check = file if not check_archive else os.path.basename(file)
        if file_to_check not in referenced_files and file not in referenced_files:
            unused_files.append(file)
    
    print(f"\n{'=' * 60}")
    print(f"Found {len(unused_files)} unused files")
    print(f"{'=' * 60}\n")
    
    if unused_files:
        # Create bak directory if it doesn't exist
        if check_archive:
            bak_dir = os.path.join(files_dir, 'archive', 'bak')
        else:
            bak_dir = os.path.join(files_dir, 'bak')
        
        if not dry_run:
            os.makedirs(bak_dir, exist_ok=True)
        
        print("Unused files:")
        for file in sorted(unused_files):
            if check_archive:
                src = os.path.join(files_dir, file)
                dst = os.path.join(bak_dir, os.path.basename(file))
            else:
                src = os.path.join(files_dir, file)
                dst = os.path.join(bak_dir, file)
            
            if dry_run:
                print(f"  [DRY RUN] Would move: {file}")
            else:
                try:
                    shutil.move(src, dst)
                    print(f"  ✓ Moved: {file}")
                except Exception as e:
                    print(f"  ✗ Error moving {file}: {e}")
    else:
        print("All files are being used! No files to move.")
    
    # Show used files
    used_files = [f for f in all_files if f in referenced_files or os.path.basename(f) in referenced_files]
    if used_files:
        print(f"\n{'=' * 60}")
        print(f"Used files ({len(used_files)}):")
        print(f"{'=' * 60}")
        for file in sorted(used_files):
            print(f"  ✓ {file}")

if __name__ == "__main__":
    import sys
    
    # Get the root directory (parent of code directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    files_dir = os.path.join(root_dir, 'files')
    
    # Parse arguments
    dry_run = True
    check_archive = False
    
    for arg in sys.argv[1:]:
        if arg == '--execute':
            dry_run = False
        elif arg == '--archive':
            check_archive = True
    
    if dry_run:
        print("DRY RUN MODE: No files will be moved. Use --execute to move files.")
    else:
        print("EXECUTE MODE: Files will be moved!")
    
    if check_archive:
        print("Checking archive directory...")
    
    print(f"\nRoot directory: {root_dir}")
    print(f"Files directory: {files_dir}\n")
    
    move_unused_files(root_dir, files_dir, dry_run, check_archive)
