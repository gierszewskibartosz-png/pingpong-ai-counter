import logging
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings
from src.routes import game, video

# Configure logging
logging.basicConfig(
    level=settings.log_level,
    format=settings.log_format
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description='Real-time AI Ping Pong Point Counter',
    version='0.1.0',
    debug=settings.debug
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Include routers
app.include_router(game.router)
app.include_router(video.router)

# Health check endpoint
@app.get('/health')
async def health_check():
    return {
        'status': 'healthy',
        'app': settings.app_name,
        'environment': settings.app_env,
        'version': '0.1.0'
    }

# Root endpoint
@app.get('/')
async def root():
    return {
        'message': 'Ping Pong AI Counter API',
        'docs': '/docs',
        'health': '/health',
        'api_version': '0.1.0'
    }

if __name__ == '__main__':
    import uvicorn
    logger.info(f'Starting {settings.app_name} on {settings.api_host}:{settings.api_port}')
    uvicorn.run(
        'src.main:app',
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_reload,
        log_level=settings.log_level.lower()
    )
