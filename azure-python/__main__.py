import pulumi
from pulumi_azure import core, compute, storage, network

# Create an Azure Resource Group
resource_group = core.ResourceGroup("eastus_update", 
    location='EastUS')

# Create an Azure resource (Storage Account)
account = storage.Account("storageEastus", 
    resource_group_name=resource_group.name,
    location=resource_group.location,
    account_tier='Standard',
    account_replication_type='ZRS')

# Export the connection string for the storage account
pulumi.export('connection_string', account.primary_connection_string)