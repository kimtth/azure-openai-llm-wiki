
$ModuleName = 'AzureRm'

if (Get-Module -ListAvailable -Name $ModuleName) {
    Write-Host "Module exists " $ModuleName
    Uninstall-Module -Name AzureRm -AllVersions -Force
} else {
    Write-Host "Module does not exist " $ModuleName
}

$ModuleName = 'Az'

if (Get-Module -ListAvailable -Name $ModuleName) {
    Write-Host "Module exists " $ModuleName
} else {
    Write-Host "Module does not exist " $ModuleName
    Install-Module Az -AllowClobber 
}

Import-Module Az

Connect-AzAccount -Tenant '<The tenant id in your env>' -SubscriptionId '<The subscription id in your env>'

Get-AzADUser -SignedIn

# cd .\azure-search-openai-demo

