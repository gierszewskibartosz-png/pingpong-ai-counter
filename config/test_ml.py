import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv(dotenv_path=project_root / '.env')

from azure.ai.ml import MLClient
from azure.identity import AzureCliCredential

def test_ml_workspace():
    """Test Azure ML Workspace connection"""
    try:
        subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
        resource_group = os.getenv('AZURE_RESOURCE_GROUP')
        workspace_name = os.getenv('AZURE_ML_WORKSPACE')
        
        if not all([subscription_id, resource_group, workspace_name]):
            print('ERROR: Missing ML configuration in .env')
            print(f'  AZURE_SUBSCRIPTION_ID: {subscription_id}')
            print(f'  AZURE_RESOURCE_GROUP: {resource_group}')
            print(f'  AZURE_ML_WORKSPACE: {workspace_name}')
            return False
        
        print('Connecting to Azure ML Workspace...')
        print(f'Using Azure CLI credentials')
        
        # Create ML client using Azure CLI credential (you're already logged in)
        credential = AzureCliCredential()
        ml_client = MLClient(
            credential=credential,
            subscription_id=subscription_id,
            resource_group_name=resource_group,
            workspace_name=workspace_name
        )
        
        # Get workspace info
        ws = ml_client.workspaces.get(workspace_name)
        
        print(f'Connected to Azure ML Workspace!')
        print(f'Workspace: {ws.name}')
        print(f'Region: {ws.location}')
        print(f'Resource Group: {resource_group}')
        
        return True
    
    except Exception as e:
        print(f'ERROR: {str(e)}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_ml_workspace()
    if success:
        print('')
        print('Azure ML Workspace connection test PASSED')
    else:
        print('')
        print('Azure ML Workspace connection test FAILED')
