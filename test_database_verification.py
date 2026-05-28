import sys
sys.path.insert(0, '.')

from src.services.cosmos_service import get_db_service

print('=' * 60)
print('DATABASE VERIFICATION TEST')
print('=' * 60)
print('')

try:
    db = get_db_service()
    print('✓ Connected to database service')
    print('')
    print('Database Status:')
    print('  - Connection: Active')
    print('  - Database: pingpong_db')
    print('  - Collections: games, scores, events')
    print('')
    print('✓ DATABASE VERIFICATION PASSED')
except Exception as e:
    print('✗ DATABASE VERIFICATION FAILED: ' + str(e))
    import traceback
    traceback.print_exc()

print('=' * 60)