from fastapi import APIRouter

router = APIRouter(prefix='/api/video', tags=['video'])

@router.post('/stream')
async def start_video_stream(source: str):
    return {
        'status': 'streaming',
        'source': source
    }

@router.get('/status')
async def get_video_status():
    return {
        'status': 'idle',
        'frames_processed': 0
    }