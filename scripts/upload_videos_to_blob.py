
import os
import sys
from pathlib import Path

sys.path.insert(0, '.')

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

def upload_videos_to_blob():
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    container_name = 'training-videos'
    local_dir = r'C:\Users\SXGIERSB\Documents\pingpong-ai-counter\data\training\cut_videos'
    
    if not connection_string:
        print('ERROR: AZURE_STORAGE_CONNECTION_STRING not found in .env')
        return False
    
    print('=' * 70)
    print('UPLOADING VIDEO SEGMENTS TO AZURE BLOB STORAGE')
    print('=' * 70)
    print('')
    
    try:
        # Connect to blob storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        print(f'Connected to Blob Storage')
        print(f'Container: {container_name}')
        print('')
        
        # Get all video files
        video_files = sorted(Path(local_dir).glob('segment_*.mp4'))
        
        if not video_files:
            print('✗ No video files found in ' + local_dir)
            return False
        
        print(f'Found {len(video_files)} video segments to upload')
        print('')
        
        # Upload each file
        upload_count = 0
        total_size = 0
        
        for video_file in video_files:
            file_name = video_file.name
            file_size_mb = video_file.stat().st_size / (1024 * 1024)
            total_size += file_size_mb
            
            print(f'Uploading: {file_name} ({file_size_mb:.1f} MB)')
            print(f'  Status: ', end='', flush=True)
            
            try:
                with open(video_file, 'rb') as data:
                    container_client.upload_blob(file_name, data, overwrite=True)
                print('✓ Success')
                upload_count += 1
            except Exception as e:
                print(f'✗ Failed: {str(e)}')
            
            print('')
        
        print('=' * 70)
        print('UPLOAD COMPLETE')
        print('=' * 70)
        print(f'Uploaded: {upload_count}/{len(video_files)} files')
        print(f'Total size: {total_size:.1f} MB')
        print(f'Container: {container_name}')
        print('')
        print('✓ Videos ready for annotation and training')
        
        return True
    
    except Exception as e:
        print(f'✗ ERROR: {str(e)}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = upload_videos_to_blob()
    sys.exit(0 if success else 1)
