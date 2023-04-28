// Copyright (c) Microsoft. All rights reserved.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using Castle.Core.Logging;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.CoreSkills;
using Microsoft.SemanticKernel.Orchestration;
using Microsoft.SemanticKernel.Planning.Planners;

namespace semanticKernelCosmos;
internal class MemoryContextAndPlanner
{
    public async Task ContextRunAsync()
    {
        var settings = new KeySettings();
        var kb = new CosmosDBKernelBuild(settings);
        var kernel = await kb.RunAsync().ConfigureAwait(true);

        Console.WriteLine("======== Context ========");
        // Create a semantic function
        var fixit = kernel.CreateSemanticFunction(
        @"I tried parsing this {{$format}} string and got an exception: {{$error}}.
        Fix the {{$format}} syntax to address the error.
        Value to fix: {{$input}}", maxTokens: 1024);

        // Setup the context
        var context = kernel.CreateNewContext();
        context["format"] = "JSON";
        context["input"] = "{ 'field': 'value";

        // Show the original broken JSON
        Console.WriteLine($"Original value: {context}");

        try
        {
            // Try to parse the JSON
            var data = JsonSerializer.Deserialize<dynamic>(context["input"]);
        }
        catch (Exception e)
        {
            // Show the error
            Console.WriteLine($"Exception: {e.Message}");

            // Capture the error message and pass it to AI
            context["error"] = e.Message;

            // Run the semantic function, ask AI to fix the problem
            var result = await fixit.InvokeAsync(context).ConfigureAwait(true);

            // Show the new JSON, fixed by AI
            Console.WriteLine(result.Result);
        }
    }

    public async Task PlannerRunAsync()
    {
        Console.WriteLine("======== Planning ========");
        var settings = new KeySettings();
        var kb = new CosmosDBKernelBuild(settings);
        var kernel = await kb.RunAsync().ConfigureAwait(true);
        var context = kernel.CreateNewContext();

        //string folder = RepoFiles.SampleSkillsPath();
        //kernel.ImportSemanticSkillFromDirectory(folder, "SummarizeSkill");
        //kernel.ImportSemanticSkillFromDirectory(folder, "WriterSkill");
        IDictionary<string, ISKFunction> conversationSummarySkill = kernel.ImportSkill(new ConversationSummarySkill(kernel));

        var planner = new SequentialPlanner(kernel);
        var planObject = await planner.CreatePlanAsync("Write a poem about John Doe, then translate it into Italian.").ConfigureAwait(true);

        Console.WriteLine("Original plan:");
        Console.WriteLine(planObject.ToJson());

        var result = await kernel.RunAsync(planObject).ConfigureAwait(true);

        Console.WriteLine("Result:");
        Console.WriteLine(result.Result);
    }
}
