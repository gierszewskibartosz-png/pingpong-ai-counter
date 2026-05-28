import os
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()

def initialize_database():
    connection_string = os.getenv('AZURE_COSMOS_CONNECTION_STRING')
    
    if not connection_string:
        print('ERROR: AZURE_COSMOS_CONNECTION_STRING not found')
        return False
    
    try:
        # Connect to Cosmos DB
        client = CosmosClient.from_connection_string(connection_string)
        database = client.get_database_client('pingpong_db')
        
        print('Connected to Cosmos DB')
        print('Initializing database schemas...')
        
        # Initialize games collection
        games_container = database.get_container_client('games')
        sample_game = {
            'id': 'game_template',
            'game_id': '',
            'player_1': {
                'id': 'p1',
                'name': 'Player 1',
                'jersey_color': 'red',
                'score': 0
            },
            'player_2': {
                'id': 'p2',
                'name': 'Player 2',
                'jersey_color': 'blue',
                'score': 0
            },
            'status': 'not_started',
            'start_time': datetime.utcnow().isoformat(),
            'end_time': None,
            'total_points': 0
        }
        
        try:
            games_container.upsert_item(sample_game)
            print('✓ Games collection initialized')
        except Exception as e:
            print(f'  Note: {str(e)}')
        
        # Initialize scores collection
        scores_container = database.get_container_client('scores')
        sample_score = {
            'id': 'score_template',
            'game_id': '',
            'player_id': '',
            'score': 0,
            'timestamp': datetime.utcnow().isoformat(),
            'is_current': True
        }
        
        try:
            scores_container.upsert_item(sample_score)
            print('✓ Scores collection initialized')
        except Exception as e:
            print(f'  Note: {str(e)}')
        
        # Initialize events collection
        events_container = database.get_container_client('events')
        sample_event = {
            'id': 'event_template',
            'game_id': '',
            'event_type': 'ball_detected',
            'player_id': '',
            'timestamp': datetime.utcnow().isoformat(),
            'details': {
                'ball_position': [0, 0],
                'confidence': 0.95,
                'paddle_contact': False
            }
        }
        
        try:
            events_container.upsert_item(sample_event)
            print('✓ Events collection initialized')
        except Exception as e:
            print(f'  Note: {str(e)}')
        
        print('')
        print('✓ Database initialization completed successfully!')
        return True
    
    except Exception as e:
        print(f'✗ ERROR: {str(e)}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = initialize_database()
    sys.exit(0 if success else 1)
