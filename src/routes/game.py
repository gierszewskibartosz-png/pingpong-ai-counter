from fastapi import APIRouter, HTTPException
from typing import Optional

router = APIRouter(prefix='/api/game', tags=['game'])

@router.get('/current')
async def get_current_game():
    return {
        'game_id': None,
        'status': 'no_active_game',
        'message': 'No game currently running'
    }

@router.post('/start')
async def start_game(player_1_name: str, player_2_name: str):
    return {
        'game_id': 'game_001',
        'status': 'started',
        'player_1': player_1_name,
        'player_2': player_2_name
    }

@router.get('/history')
async def get_game_history():
    return {
        'games': [],
        'total': 0
    }