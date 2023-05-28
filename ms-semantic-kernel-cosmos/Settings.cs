// Copyright (c) Microsoft. All rights reserved.

using System.Text.Json;
using System.Text.Json.Serialization;

namespace semanticKernelCosmos;

internal class Settings
{
    public string Type { get; set; }
    public string Model { get; set; }
    public string EndPoint { get; set; }
    public string AOAIApiKey { get; set; } // Azure Open AI
    public string OAIApiKey { get; set; } // Open AI
    public string OrdId { get; set; }
    public string BingSearchAPIKey { get; set; }
    public string aoaiDomainName { get; set; }
    public string CosmosConnectionString { get; set; }
}

internal class KeySettings
{
    public Settings ApiKeySettings()
    {
        Console.WriteLine(Directory.GetCurrentDirectory());
        // Read the JSON file into a string
        string workingDirectory = Environment.CurrentDirectory;
        string projectDirectory = Directory.GetParent(workingDirectory).Parent.Parent.FullName;
        string inputPath = Path.Combine(projectDirectory, "appsettings.json");
        string json = File.ReadAllText(inputPath);

        // Deserialize the JSON string into a C# object
        Settings settings = JsonSerializer.Deserialize<Settings>(json);

        // Print the properties of the C# object
        // Console.WriteLine($"Type: {settings.Type}");
        Console.WriteLine($"Json Loaded: {settings.Type}");

        return settings;
    }
}
