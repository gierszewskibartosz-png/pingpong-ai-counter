import requests

print('Testing API endpoints...')
print('')

base_url = 'http://localhost:8000'

# Test 1: Health
print('1. Health Endpoint:')
try:
    response = requests.get(base_url + '/health')
    print('   Status Code: ' + str(response.status_code))
    print('   Response: ' + response.text)
except Exception as e:
    print('   Error: ' + str(e))

print('')

# Test 2: Root
print('2. Root Endpoint:')
try:
    response = requests.get(base_url + '/')
    print('   Status Code: ' + str(response.status_code))
    print('   Response: ' + response.text)
except Exception as e:
    print('   Error: ' + str(e))

print('')

# Test 3: Game
print('3. Game Endpoint:')
try:
    response = requests.get(base_url + '/api/game/current')
    print('   Status Code: ' + str(response.status_code))
    print('   Response: ' + response.text)
except Exception as e:
    print('   Error: ' + str(e))

print('')
print('All endpoint tests completed!')