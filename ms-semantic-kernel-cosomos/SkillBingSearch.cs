// Copyright (c) Microsoft. All rights reserved.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.Cosmos;
using Microsoft.SemanticKernel.Connectors.Memory.AzureCosmosDb;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Skills.Web.Bing;
using Microsoft.SemanticKernel.Skills.Web;

namespace semanticKernelCosmos;
internal class SkillBingSearch
{
    public async Task RunAsync()
    {
        var settings = new KeySettings();
        var values = settings.ApiKeySettings();

        var model = values.Model;
        var azureEndpoint = values.EndPoint;
        var apiKey = values.AOAIApiKey;
        var bingSearchAPIKey = values.BingSearchAPIKey;
        var aoaiDomainName = values.aoaiDomainName;
        var connectionString = values.CosmosConnectionString;

        Console.WriteLine("start");

        Console.WriteLine("== Connect the collection in DB ==");

        using (CosmosClient cosmosClient = new(connectionString))
        {
            string MemoryDatabaseName = "vectorStore";
            var memStore = await CosmosMemoryStore.CreateAsync(cosmosClient, MemoryDatabaseName).ConfigureAwait(true);

            IKernel kernel = Kernel.Builder
                .Configure(c =>
                {
                    c.AddAzureTextEmbeddingGenerationService(aoaiDomainName, "embed", azureEndpoint, apiKey);
                    c.AddAzureTextCompletionService(aoaiDomainName, model, azureEndpoint, apiKey);
                })
                .WithMemoryStorage(memStore)
                .Build();

            using var bingConnector = new BingConnector(bingSearchAPIKey);
            var webSearchEngineSkill = new WebSearchEngineSkill(bingConnector);
            var web = kernel.ImportSkill(webSearchEngineSkill);

            // Run
            var ask = "What's the tallest building in Europe?";
            var result = await kernel.RunAsync(
                ask,
                web["SearchAsync"]
            ).ConfigureAwait(true);

            Console.WriteLine(ask + "\n");
            Console.WriteLine(result);
        }
    }
}
