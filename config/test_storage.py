import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_blob_storage():
    """Test Azure Blob Storage connection"""
    try:
        # Get connection string from .env
        connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        
        if not connection_string:
            print('ERROR: AZURE_STORAGE_CONNECTION_STRING not found in .env')
            return False
        
        # Create blob service client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # List containers
        print('✓ Connected to Azure Blob Storage!')
        print('✓ Storage Account: pingpongstorage2026')
        print('✓ Containers:')
        for container in blob_service_client.list_containers():
            print(f'  - {container.name}')
        
        return True
    
    except Exception as e:
        print(f'✗ ERROR: {str(e)}')
        return False

if __name__ == '__main__':
    success = test_blob_storage()
    if success:
        print('\n✓ Blob Storage connection test PASSED')
    else:
        print('\n✗ Blob Storage connection test FAILED')
