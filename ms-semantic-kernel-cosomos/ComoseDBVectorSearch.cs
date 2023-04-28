// Copyright (c) Microsoft. All rights reserved.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.Cosmos;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.Memory.AzureCosmosDb;
using Microsoft.SemanticKernel.Memory;

namespace semanticKernelCosmos;
internal class ComoseDBVectorSearch
{
    public async Task RunAsync()
    {
        var settings = new KeySettings();
        var kb = new CosmosDBKernelBuild(settings);
        var kernel = await kb.RunAsync().ConfigureAwait(true);

        string MemoryCollectionName = "vectorCollection";
        Console.WriteLine("== Similarity Searching Memories: My favorite color is orange ==");
        var searchResults = kernel.Memory.SearchAsync(MemoryCollectionName, "british", limit: 3, minRelevanceScore: 0.8);

        var i = 0;
        await foreach (MemoryQueryResult memory in searchResults)
        {
            Console.WriteLine($"Result {++i}:");
            Console.WriteLine("  URL:     : " + memory.Metadata.Id);
            Console.WriteLine("  Title    : " + memory.Metadata.Description);
            Console.WriteLine("  Relevance: " + memory.Relevance);
            Console.WriteLine();
        }
    }
}
