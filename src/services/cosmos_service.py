import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

sys.path.insert(0, str(Path(__file__).parent.parent))

from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()

class CosmosDBService:
    def __init__(self):
        self.connection_string = os.getenv('AZURE_COSMOS_CONNECTION_STRING')
        self.client = None
        self.database = None
        self.connect()
    
    def connect(self):
        if not self.connection_string:
            raise ValueError('AZURE_COSMOS_CONNECTION_STRING not set')
        self.client = CosmosClient.from_connection_string(self.connection_string)
        self.database = self.client.get_database_client('pingpong_db')
    
    # Games operations
    def create_game(self, game_data: Dict) -> Dict:
        container = self.database.get_container_client('games')
        return container.create_item(body=game_data)
    
    def get_game(self, game_id: str) -> Optional[Dict]:
        container = self.database.get_container_client('games')
        try:
            return container.read_item(item=game_id, partition_key=game_id)
        except:
            return None
    
    def update_game(self, game_data: Dict) -> Dict:
        container = self.database.get_container_client('games')
        return container.upsert_item(body=game_data)
    
    # Scores operations
    def save_score(self, score_data: Dict) -> Dict:
        container = self.database.get_container_client('scores')
        return container.create_item(body=score_data)
    
    def get_latest_score(self, game_id: str) -> Optional[Dict]:
        container = self.database.get_container_client('scores')
        query = 'SELECT * FROM c WHERE c.game_id = @game_id ORDER BY c.timestamp DESC OFFSET 0 LIMIT 1'
        results = list(container.query_items(query=query, parameters=[{'name': '@game_id', 'value': game_id}]))
        return results[0] if results else None
    
    # Events operations
    def log_event(self, event_data: Dict) -> Dict:
        container = self.database.get_container_client('events')
        return container.create_item(body=event_data)
    
    def get_game_events(self, game_id: str, limit: int = 100) -> List[Dict]:
        container = self.database.get_container_client('events')
        query = 'SELECT * FROM c WHERE c.game_id = @game_id ORDER BY c.timestamp DESC OFFSET 0 LIMIT @limit'
        return list(container.query_items(query=query, parameters=[{'name': '@game_id', 'value': game_id}, {'name': '@limit', 'value': limit}]))

# Singleton instance
_db_service = None

def get_db_service() -> CosmosDBService:
    global _db_service
    if _db_service is None:
        _db_service = CosmosDBService()
    return _db_service
