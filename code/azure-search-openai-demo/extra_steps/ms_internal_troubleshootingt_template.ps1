# The command listing if the open ai services are remained to be purged.
# az cognitiveservices account list-deleted
# Azure Portal > .. > Open AI > Click "Manage deleted resources" > Select the specific service > Click "Purge"

az account set --subscription "<your_subscription_name>"

az ad signed-in-user show

<# 
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
  "businessPhones": [],
  "displayName": "<The value in your env>",
  "givenName": "<The value in your env>",
  "id": "<The value in your env>",
  "jobTitle": "<The value in your env>",
  "mail": "<The value in your env>",
  "mobilePhone": null,
  "officeLocation": "<The value in your env>",
  "preferredLanguage": null,
  "surname": "<The value in your env>",
  "userPrincipalName": "<The value in your env>"
}
#>

# !important: The value in "id" == Principle Id

az account show

<#
{
  "environmentName": "AzureCloud",
  "homeTenantId": "<The value in your env>",
  "id": "<The value in your env>",
  "isDefault": true,
  "managedByTenants": [],
  "name": "<The value in your env>",
  "state": "Enabled",
  "tenantId": "<The value in your env>",
  "user": {
    "name": "<The value in your env>",
    "type": "user"
  }
}
#>

# Please execute the following command on Project directory. ex) PS .\azure-search-openai-demo>
azd env set AZURE_PRINCIPAL_ID "<Principle Id>"

# Please execute the following command on Project directory. ex) PS .\azure-search-openai-demo>
azd up

# Launch the server locally 
# > cd app
# > start.cmd