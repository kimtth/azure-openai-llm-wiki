using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Memory;
using Microsoft.Azure.Cosmos;
using Microsoft.SemanticKernel.Connectors.Memory.AzureCosmosDb;
using Microsoft.Azure.Cosmos.Serialization.HybridRow.Layouts;
using System.Runtime.CompilerServices;

namespace semanticKernelCosmos;
internal class CosmosDBVectorStore
{

    private IKernel _kernel;
    public static async Task RunAsync()
    {
        var settings = new KeySettings();
        var kb = new CosmosDBKernelBuild(settings);
        var kernel = await kb.RunAsync().ConfigureAwait(true);

        Console.WriteLine("== Adding Memories ==");

        string MemoryCollectionName = "vectorCollection";
        var key1 = await kernel.Memory.SaveInformationAsync(MemoryCollectionName, id: "cat1", text: "british short hair").ConfigureAwait(true);
        var key2 = await kernel.Memory.SaveInformationAsync(MemoryCollectionName, id: "cat2", text: "orange tabby").ConfigureAwait(true);
        var key3 = await kernel.Memory.SaveInformationAsync(MemoryCollectionName, id: "cat3", text: "norwegian forest cat").ConfigureAwait(true);

        Console.WriteLine("== Retrieving Memories Through the Kernel ==");
        MemoryQueryResult lookup = await kernel.Memory.GetAsync(MemoryCollectionName, "cat1").ConfigureAwait(true);
        Console.WriteLine(lookup != null ? lookup.Metadata.Text : "ERROR: memory not found");

        Console.WriteLine("end");
    }

    public async Task<IKernel> InitializeKernelAsync()
    {
        var settings = new KeySettings();
        var kb = new CosmosDBKernelBuild(settings);
        var kernel = await kb.RunAsync().ConfigureAwait(true);

        return kernel;
    }

    public async Task SaveLineRunAsync(int id, string text)
    {
        Console.WriteLine("== Adding Memories ==");
        if (this._kernel is null)
        {
            this._kernel = await this.InitializeKernelAsync().ConfigureAwait(true);
        }
        string MemoryCollectionName = "vectorCollection";
        var key1 = await this._kernel.Memory.SaveInformationAsync(MemoryCollectionName, id: id.ToString(), text: text).ConfigureAwait(true);
    }
}



