using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace semanticKernelCosmos;
internal class Program
{
    private static async Task Main(string[] args)
    {
        //var runDemo = new ComoseDBVectorSearch();
        var runDemo = new SkillBingSearch();
        //var runDemo = new SemanticFunction();
        //var runDemo = new MemoryConversationHistory();
        await runDemo.RunAsync().ConfigureAwait(true);


        //var td = new MemoryContextAndPlanner();
        //await td.ContextRunAsync().ConfigureAwait(true);
        //await td.PlannerRunAsync().ConfigureAwait(true);


        //
        //var runDemo = new LoadDocumentPage();
        //runDemo.FuncCheckProcess();

        //string workingDirectory = Environment.CurrentDirectory;
        //string projectDirectory = Directory.GetParent(workingDirectory).Parent.Parent.FullName;
        //string inputPath = Path.Combine(projectDirectory, "data\\all_pdf_2022.pdf");
        //var rtn = runDemo.SplitTextToParagraphSection(inputPath);
        //string outputPath = Path.Combine(projectDirectory, "output.txt");

        // File.WriteAllText(outputPath, "");
        //foreach (var line in rtn)
        //{
        //    string cleanedline = line.Item1;
        //    Console.WriteLine(cleanedline);
        //    Console.WriteLine();
        //    File.AppendAllText(outputPath, cleanedline + Environment.NewLine + Environment.NewLine);
        //}
    }
}
