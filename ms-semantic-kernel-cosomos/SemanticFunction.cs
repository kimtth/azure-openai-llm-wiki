// Copyright (c) Microsoft. All rights reserved.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.Cosmos;
using Microsoft.SemanticKernel;

namespace semanticKernelCosmos;
internal class SemanticFunction
{
    public async Task RunAsync()
    {

        var settings = new KeySettings();
        var kb = new CosmosDBKernelBuild(settings);
        var kernel = await kb.RunAsync().ConfigureAwait(true);

        string skPrompt = @"
        {{$input}}

        Give me the TLDR in 5 words.
        ";

        var textToSummarize = @"
        1) A robot may not injure a human being or, through inaction,
        allow a human being to come to harm.

        2) A robot must obey orders given it by human beings except where
        such orders would conflict with the First Law.

        3) A robot must protect its own existence as long as such protection
        does not conflict with the First or Second Law.
        "
        ;

        // Example09_FunctionTypes.cs
        // https://github.com/microsoft/semantic-kernel/blob/main/dotnet/README.md

        // 1
        var tldrFunction = kernel.CreateSemanticFunction(skPrompt, maxTokens: 200, temperature: 0, topP: 0.5);

        var summary = await kernel.RunAsync(
            textToSummarize,
            tldrFunction
        ).ConfigureAwait(true);
        Console.WriteLine(summary);

        // 2
        var func = kernel.CreateSemanticFunction(
            "List the two planets closest to '{{$input}}', excluding moons, using bullet points.");

        var result = await func.InvokeAsync("Jupiter").ConfigureAwait(true);
        Console.WriteLine(result);
    }

}
