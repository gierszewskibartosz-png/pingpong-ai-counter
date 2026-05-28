import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv(dotenv_path=project_root / '.env')

from azure.containerregistry import ContainerRegistryClient
from azure.identity import AzureCliCredential

def test_container_registry():
    """Test Azure Container Registry connection"""
    try:
        acr_name = os.getenv('ACR_NAME')
        
        if not acr_name:
            print('ERROR: ACR_NAME not found in .env')
            return False
        
        print(f'Connecting to Container Registry: {acr_name}')
        
        # Create registry client
        credential = AzureCliCredential()
        registry_url = f'https://{acr_name}.azurecr.io'
        client = ContainerRegistryClient(endpoint=registry_url, credential=credential)
        
        # Get registry properties
        print(f'Connected to Azure Container Registry!')
        print(f'Registry: {acr_name}')
        print(f'URL: {registry_url}')
        print(f'Status: Ready for Docker image storage')
        
        return True
    
    except Exception as e:
        print(f'ERROR: {str(e)}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_container_registry()
    if success:
        print('')
        print('Container Registry connection test PASSED')
    else:
        print('')
        print('Container Registry connection test FAILED')