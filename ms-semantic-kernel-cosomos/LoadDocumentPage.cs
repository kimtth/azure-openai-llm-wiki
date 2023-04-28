// Copyright (c) Microsoft. All rights reserved.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.PortableExecutable;
using System.IO;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using iTextSharp.text;
using iTextSharp.text.pdf;
using iTextSharp.text.pdf.parser;
using Path = System.IO.Path;
using System.Text;

namespace semanticKernelCosmos;
internal class LoadDocumentPage
{
    private readonly int _max_section_length = 1000;
    private readonly int _sentence_search_limit = 100;
    private readonly int _section_overlap = 100;

    public void FuncCheckProcess()
    {
        // The path of the input PDF file
        string workingDirectory = Environment.CurrentDirectory;
        string projectDirectory = Directory.GetParent(workingDirectory).Parent.Parent.FullName;
        string inputPath = Path.Combine(projectDirectory, "data\\000463185.pdf");
        string outputPath = Path.Combine(projectDirectory, "output");

        // The pattern to split text into sentences
        string[] separators = { "! ", "?", "。" };
        
        // Create a reader for the input PDF file
        PdfReader reader = new PdfReader(inputPath);
        // Get the number of pages in the PDF file
        int pageCount = reader.NumberOfPages;

        // Loop through each page
        for (int i = 1; i <= pageCount; i++)
        {
            // Create a document for the output PDF file
            Document document = new Document();
            // Create a writer for the output PDF file
            string zeroFillnum = i.ToString().PadLeft(3, '0');
            FileStream os = new(Path.Combine(outputPath, $"page{zeroFillnum}.pdf"), FileMode.Create);
            PdfWriter writer = PdfWriter.GetInstance(document, os: os);
            // Open the document
            document.Open();
            // Copy the page from the input PDF file to the output PDF file
            PdfImportedPage page = writer.GetImportedPage(reader, i);
            writer.DirectContent.AddTemplate(page, 0, 0);
            // Close the document
            document.Close();

            // Create a strategy for extracting text from the page
            ITextExtractionStrategy strategy = new SimpleTextExtractionStrategy();
            // Extract the text from the page
            string text = PdfTextExtractor.GetTextFromPage(reader, i, strategy);

            // Unicode Normalize 
            text = text.Normalize(NormalizationForm.FormKC);
            text = text.Replace(System.Environment.NewLine, string.Empty).Replace("\n", string.Empty).Replace("\n", string.Empty);
            // Split the text into sentences using Regex
            string[] sentences = text.Split(separators, StringSplitOptions.RemoveEmptyEntries);

            // Loop through each sentence and print it to the console
            int j = 0;
            foreach (string sentence in sentences)
            {
                string cleanSentence = sentence.Replace(" ", "").Replace(System.Environment.NewLine, string.Empty);
                Console.WriteLine(cleanSentence);
                // File.AppendAllText("output.txt", $"{j}: {cleanSentence}" + "\n\n");
                //File.AppendAllText("output.txt", $"{j}: {cleanSentence}" + "\n\n");
                j++;
            }
        }

        // Close the reader
        reader.Close();
    }

    private string TextClean(string text)
    {
        // Unicode Normalize 
        text = text.Normalize(NormalizationForm.FormKC);

        // Multiple spaces and dot pattern take out
        string spacePattern = @"\s{2,}";
        string dotPattern = @"\.{2,}";
        string replacement = " ";
        string cleanedline = Regex.Replace(text, dotPattern, replacement);
        cleanedline = Regex.Replace(cleanedline, spacePattern, replacement);
        cleanedline = cleanedline.Replace(System.Environment.NewLine, string.Empty).Replace("\n", string.Empty).Replace("\n", string.Empty);

        return cleanedline;
    }

    public List<(string, int)> SplitTextToParagraphSection(string inputPath)
    {
        List<(string, int)> sections = new List<(string, int)>();

        string[] SENTENCE_ENDINGS = new string[] { ".", "。", "!", "?" };
        string[] WORDS_BREAKS = new string[] { ",", ";", ":", " ", "(", ")", "[", "]", "{", "}", "\t", "\n" };
        Console.WriteLine($"Splitting '{inputPath}' into sections");

        PdfReader reader = new(inputPath);
        ITextExtractionStrategy strategy = new SimpleTextExtractionStrategy();
        int pageCount = reader.NumberOfPages;

        // Prep: Store text and text length by unit of page
        List<(int, int, string)> page_map = new List<(int, int, string)>();
        int offset = 0;
        for (int i = 1; i <= pageCount; i++)
        {
            string text = PdfTextExtractor.GetTextFromPage(reader, i, strategy);
            text = this.TextClean(text);
            page_map.Add((i, offset, text));
            offset += text.Length;
        }

        // Utility to provide information about the text coming from which page. 
        int FindPage(int offset)
        {
            int l = page_map.Count;
            for (int i = 0; i < l - 1; i++)
            {
                // if offset >= page_map[i][1] and offset < page_map[i + 1][1]:
                if (offset >= page_map[i].Item2 && offset < page_map[i + 1].Item2)
                {
                    return i;
                }
            }
            return l - 1;
        }

        // Proc: Consolidate all text in the document.
        string all_text = string.Concat(page_map.Select(p => p.Item3));
        int length = all_text.Length;
        int start = 0;
        int end = length;
        while (start + this._section_overlap < length)
        {
            int last_word = -1;
            end = start + this._max_section_length;

            if (end > length)
            {
                end = length;
            }
            else
            {
                // Try to find the end of the sentence
                while (end < length && (end - start - this._max_section_length) < this._sentence_search_limit && !SENTENCE_ENDINGS.Contains(all_text[end].ToString()))
                {
                    if (WORDS_BREAKS.Contains(all_text[end].ToString()))
                    {
                        last_word = end;
                    }
                    end++;
                }
                if (end < length && !SENTENCE_ENDINGS.Contains(all_text[end].ToString()) && last_word > 0)
                {
                    end = last_word; // Fall back to at least keeping a whole word
                }
            }
            if (end < length)
            {
                end++;
            }

            // Try to find the start of the sentence or at least a whole word boundary
            last_word = -1;
            while (start > 0 && start > end - this._max_section_length - 2 * this._sentence_search_limit && !SENTENCE_ENDINGS.Contains(all_text[start].ToString()))
            {
                if (WORDS_BREAKS.Contains(all_text[start].ToString()))
                {
                    last_word = start;
                }
                start--;
            }
            if (!SENTENCE_ENDINGS.Contains(all_text[start].ToString()) && last_word > 0)
            {
                start = last_word;
            }
            if (start > 0)
            {
                start++;
            }

            //Console.WriteLine("==========================><");
            //Console.WriteLine(all_text.Substring(start, end - start), FindPage(start));
            sections.Add((all_text.Substring(start, end - start), FindPage(start)));
            start = end - this._section_overlap;
        }

        if (start + this._section_overlap < end)
        {
            //Console.WriteLine("==========================><last");
            //Console.WriteLine(all_text.Substring(start, end - start), FindPage(start));
            sections.Add((all_text.Substring(start, end - start), FindPage(start)));
        }

        return sections;
    }

}
