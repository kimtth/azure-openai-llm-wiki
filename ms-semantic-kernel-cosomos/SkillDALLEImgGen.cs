// Copyright (c) Microsoft. All rights reserved.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.Cosmos;
using Microsoft.SemanticKernel.Connectors.Memory.AzureCosmosDb;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.AI.ImageGeneration;

namespace semanticKernelCosmos;
internal class SkillDALLEImgGen
{
    public async Task RunAsync()
    {
        var kernel = await InitializeKernelAsync().ConfigureAwait(true);

        IImageGeneration dallE = kernel.GetService<IImageGeneration>();

        var imageDescription = "A cute baby sea otter";
        var image = await dallE.GenerateImageAsync(imageDescription, 256, 256).ConfigureAwait(true);

        Console.WriteLine(imageDescription);
        Console.WriteLine("Image URL: " + image);
    }

    private static async Task<IKernel> InitializeKernelAsync()
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
                    c.AddOpenAIImageGenerationService("dallE", apiKey);
                })
                .WithMemoryStorage(memStore)
                .Build();

            return kernel;
        }
    }
}
