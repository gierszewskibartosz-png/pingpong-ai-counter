import sys
sys.path.insert(0, '.')

from src.services.cosmos_service import get_db_service
from datetime import datetime
import uuid

print('Testing Cosmos DB Service...')

try:
    # Get service
    db = get_db_service()
    print('Connected to database service')
    
    # Test creating a game
    game_id = str(uuid.uuid4())[:8]
    game = {
        'id': game_id,
        'game_id': game_id,
        'player_1': {'name': 'Test Player 1', 'jersey_color': 'red', 'score': 0},
        'player_2': {'name': 'Test Player 2', 'jersey_color': 'blue', 'score': 0},
        'status': 'test',
        'start_time': datetime.utcnow().isoformat()
    }
    
    result = db.create_game(game)
    print('Created test game: ' + game_id)
    
    # Test retrieving game
    retrieved = db.get_game(game_id)
    if retrieved:
        game_id_retrieved = retrieved['id']
        print('Retrieved game: ' + game_id_retrieved)
    
    print('')
    print('Cosmos DB Service test PASSED')
    
except Exception as e:
    print('ERROR: ' + str(e))
    import traceback
    traceback.print_exc()
