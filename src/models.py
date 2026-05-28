from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Game Models
class Player(BaseModel):
    id: str
    name: str
    jersey_color: str
    score: int = 0

class GameScore(BaseModel):
    player_1: Player
    player_2: Player
    timestamp: datetime

class GameEvent(BaseModel):
    event_type: str
    player_id: str
    timestamp: datetime
    details: dict

class GameState(BaseModel):
    game_id: str
    player_1: Player
    player_2: Player
    current_score: GameScore
    events: List[GameEvent] = []
    status: str
    start_time: datetime
    end_time: Optional[datetime] = None

# Video Models
class VideoStreamRequest(BaseModel):
    source: str
    name: str

class DetectionResult(BaseModel):
    ball_position: tuple
    paddles: dict
    confidence: float
    timestamp: datetime

# API Response Models
class HealthResponse(BaseModel):
    status: str
    app: str
    environment: str
    version: str