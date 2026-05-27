import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Load .env file manually
from dotenv import load_dotenv

env_path = project_root / '.env'
print(f'Loading .env from: {env_path}')
load_dotenv(dotenv_path=env_path, verbose=True)

from azure.cosmos import CosmosClient

def test_cosmos_db():
    """Test Azure Cosmos DB connection"""
    try:
        # Get connection string from environment
        connection_string = os.getenv('AZURE_COSMOS_CONNECTION_STRING')
        
        if not connection_string:
            print('ERROR: AZURE_COSMOS_CONNECTION_STRING not found in .env')
            print('Available env vars:')
            for key in os.environ:
                if 'COSMOS' in key or 'AZURE' in key:
                    print(f'  {key}')
            return False
        
        print(f'Connection string found')
        print(f'Length: {len(connection_string)}')
        print(f'Starts with: {connection_string[:50]}...')
        print(f'Ends with: ...{connection_string[-50:]}')
        
        # Create Cosmos DB client
        print('Creating CosmosClient...')
        client = CosmosClient.from_connection_string(connection_string)
        
        # Test connection by listing databases
        print('Listing databases...')
        databases = list(client.list_databases())
        print(f'Found {len(databases)} database(s)')
        
        # Get database
        print('Getting database: pingpong_db')
        database = client.get_database_client('pingpong_db')
        
        # List containers
        print('Connected to Azure Cosmos DB!')
        print('Database: pingpong_db')
        print('Collections:')
        containers = list(database.list_containers())
        for container in containers:
            container_id = container['id']
            print(f'  - {container_id}')
        
        return True
    
    except Exception as e:
        print(f'ERROR: {str(e)}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_cosmos_db()
    if success:
        print('')
        print('Cosmos DB connection test PASSED')
    else:
        print('')
        print('Cosmos DB connection test FAILED')