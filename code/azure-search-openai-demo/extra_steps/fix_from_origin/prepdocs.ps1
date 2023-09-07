$output = azd env get-values

foreach ($line in $output) {
  $name, $value = $line.Split("=")
  $value = $value -replace '^\"|\"$'
  [Environment]::SetEnvironmentVariable($name, $value)
}

Write-Host "Environment variables set."

# This is a comment -- add by Kim
cd .\scripts
python -m venv venv 
venv\Scripts\activate.bat
cd ..
# This is a comment -- add by Kim

pip install -r ./scripts/requirements.txt
python ./scripts/prepdocs.py './data/*' --storageaccount $env:AZURE_STORAGE_ACCOUNT --container $env:AZURE_STORAGE_CONTAINER --searchservice $env:AZURE_SEARCH_SERVICE --index $env:AZURE_SEARCH_INDEX -v
