// Copyright (c) Microsoft. All rights reserved.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.Cosmos;
using Microsoft.SemanticKernel.Connectors.Memory.AzureCosmosDb;
using Microsoft.SemanticKernel;

#pragma warning disable IDE0009 // Member access should be qualified.
namespace semanticKernelCosmos;
internal class CosmosDBKernelBuild
{
    private KeySettings _settings;
    public CosmosDBKernelBuild(KeySettings settings)
    {
        this._settings = settings;
    }

    public async Task<IKernel> RunAsync()
    {
        bool useAzureOpenAI = false;
        var values = _settings.ApiKeySettings();

        if (values.Type == "azure")
        {
            useAzureOpenAI = true;
        }

        var model = values.Model;
        var azureEndpoint = values.EndPoint;
        var apiKey = values.AOAIApiKey;
        var orgId = values.OrdId;
        var aoaiDomainName = values.aoaiDomainName;
        var connectionString = values.CosmosConnectionString;

        using (CosmosClient cosmosClient = new(connectionString))
        {
            var memStore = await CosmosCreateAsync(cosmosClient).ConfigureAwait(true);

            var kernel = new KernelBuilder()
                .Configure(c =>
                {
                    if (useAzureOpenAI)
                    {
                        c.AddAzureTextEmbeddingGenerationService(aoaiDomainName, "embed", azureEndpoint, apiKey);
                        c.AddAzureChatCompletionService(aoaiDomainName, model, azureEndpoint, apiKey); // ChatGPT
                                                                                                       // Davinci: c.AddAzureTextCompletionService(aoaiDomainName, model, azureEndpoint, apiKey);
                    }
                    else
                    {
                        c.AddOpenAITextEmbeddingGenerationService("ada", "text-embedding-ada-002", apiKey);
                        c.AddOpenAITextCompletionService("davinci", model, apiKey, orgId);
                    }
                })
                .WithMemoryStorage(memStore)
                .Build();

            return kernel;
        }
    }
    private async Task<CosmosMemoryStore> CosmosCreateAsync(CosmosClient cosmosClient)
    {
        string MemoryDatabaseName = "vectorStore";
        var memStore = await CosmosMemoryStore.CreateAsync(cosmosClient, MemoryDatabaseName).ConfigureAwait(true);

        return memStore;
    }
}
#pragma warning restore IDE0009 // Member access should be qualified.
