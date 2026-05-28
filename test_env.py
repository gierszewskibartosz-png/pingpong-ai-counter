import os
import sys
sys.path.insert(0, '.')

from dotenv import load_dotenv
load_dotenv()

app_name = os.getenv('APP_NAME')
api_port = os.getenv('API_PORT')
app_env = os.getenv('APP_ENV')

print('APP_NAME: ' + str(app_name))
print('API_PORT: ' + str(api_port))
print('APP_ENV: ' + str(app_env))
print('Environment variables loaded successfully!')