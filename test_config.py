import sys
sys.path.insert(0, '.')

try:
    from src.config import settings
    print('App: ' + settings.app_name)
    print('Env: ' + settings.app_env)
    print('API Port: ' + str(settings.api_port))
    print('Configuration loaded successfully!')
except Exception as e:
    print('ERROR: ' + str(e))
    import traceback
    traceback.print_exc()