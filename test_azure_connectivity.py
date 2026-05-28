import sys
import os
sys.path.insert(0, '.')

from dotenv import load_dotenv
load_dotenv()

print('=' * 60)
print('AZURE CONNECTIVITY TEST')
print('=' * 60)
print('')

# Test 1: Configuration
print('1. CONFIGURATION TEST')
try:
    from src.config import settings
    print('   ✓ Configuration loaded')
    print('   App: ' + settings.app_name)
    print('   Environment: ' + settings.app_env)
    print('   API Port: ' + str(settings.api_port))
except Exception as e:
    print('   ✗ Configuration failed: ' + str(e))

print('')

# Test 2: Blob Storage
print('2. BLOB STORAGE TEST')
try:
    from azure.storage.blob import BlobServiceClient
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_client = BlobServiceClient.from_connection_string(connection_string)
    containers = list(blob_client.list_containers())
    print('   ✓ Connected to Blob Storage')
    print('   Containers: ' + str(len(containers)))
    for container in containers:
        print('     - ' + container['name'])
except Exception as e:
    print('   ✗ Blob Storage failed: ' + str(e))

print('')

# Test 3: Cosmos DB
print('3. COSMOS DB TEST')
try:
    from azure.cosmos import CosmosClient
    connection_string = os.getenv('AZURE_COSMOS_CONNECTION_STRING')
    cosmos_client = CosmosClient.from_connection_string(connection_string)
    database = cosmos_client.get_database_client('pingpong_db')
    containers = list(database.list_containers())
    print('   ✓ Connected to Cosmos DB')
    print('   Collections: ' + str(len(containers)))
    for container in containers:
        print('     - ' + container['id'])
except Exception as e:
    print('   ✗ Cosmos DB failed: ' + str(e))

print('')

# Test 4: ML Workspace
print('4. AZURE ML WORKSPACE TEST')
try:
    from azure.ai.ml import MLClient
    from azure.identity import AzureCliCredential
    subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
    resource_group = os.getenv('AZURE_RESOURCE_GROUP')
    workspace_name = os.getenv('AZURE_ML_WORKSPACE')
    credential = AzureCliCredential()
    ml_client = MLClient(credential=credential, subscription_id=subscription_id, resource_group_name=resource_group, workspace_name=workspace_name)
    ws = ml_client.workspaces.get(workspace_name)
    print('   ✓ Connected to ML Workspace')
    print('   Workspace: ' + ws.name)
    print('   Region: ' + ws.location)
except Exception as e:
    print('   ✗ ML Workspace failed: ' + str(e))

print('')

# Test 5: Container Registry
print('5. CONTAINER REGISTRY TEST')
try:
    acr_name = os.getenv('ACR_NAME')
    print('   ✓ Container Registry configured')
    print('   Registry: ' + acr_name)
    print('   Login Server: ' + acr_name + '.azurecr.io')
except Exception as e:
    print('   ✗ Container Registry failed: ' + str(e))

print('')
print('=' * 60)
print('CONNECTIVITY TEST COMPLETED')
print('=' * 60)