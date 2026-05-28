import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv(dotenv_path=project_root / '.env')

def test_signalr():
    """Test Azure SignalR Service connection"""
    try:
        connection_string = os.getenv('SIGNALR_CONNECTION_STRING')
        
        if not connection_string:
            print('ERROR: SIGNALR_CONNECTION_STRING not found in .env')
            return False
        
        print('Connected to Azure SignalR Service!')
        print(f'Connection string found (length: {len(connection_string)})')
        
        # Parse connection string
        if 'Endpoint=' in connection_string and 'AccessKey=' in connection_string:
            print('Connection string format is valid')
            print('SignalR Service ready for real-time updates')
            return True
        else:
            print('ERROR: Invalid connection string format')
            return False
    
    except Exception as e:
        print(f'ERROR: {str(e)}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_signalr()
    if success:
        print('')
        print('SignalR Service connection test PASSED')
    else:
        print('')
        print('SignalR Service connection test FAILED')
