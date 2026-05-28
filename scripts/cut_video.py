
import subprocess
import os
from pathlib import Path

# FFmpeg paths
FFMPEG_PATH = r"C:\Users\SXGIERSB\Documents\pingpong-ai-counter\data\training\raw_videos\ffmpeg\bin\ffmpeg.exe"
FFPROBE_PATH = r"C:\Users\SXGIERSB\Documents\pingpong-ai-counter\data\training\raw_videos\ffmpeg\bin\ffprobe.exe"

input_file = r"C:\Users\SXGIERSB\Documents\pingpong-ai-counter\data\training\raw_videos\video_full_match.mp4"
output_dir = r"C:\Users\SXGIERSB\Documents\pingpong-ai-counter\data\training\cut_videos"
segment_length = 120  # 2 minutes

print("=" * 70)
print("PING PONG VIDEO CUTTING TOOL")
print("=" * 70)
print("")

# Verify FFmpeg exists
print("Verifying FFmpeg installation...")
if not os.path.exists(FFMPEG_PATH):
    print(f"✗ ERROR: ffmpeg not found at {FFMPEG_PATH}")
    exit(1)

if not os.path.exists(FFPROBE_PATH):
    print(f"✗ ERROR: ffprobe not found at {FFPROBE_PATH}")
    exit(1)

print("✓ FFmpeg tools found")
print("")

# Create output directory
Path(output_dir).mkdir(parents=True, exist_ok=True)
print(f"✓ Output directory: {output_dir}")
print("")

print("Analyzing video...")
print(f"Input file: {input_file}")
print("")

# Get video duration - use simpler command
cmd = [
    FFPROBE_PATH,
    "-v", "error",
    "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1:novalue=1",
    input_file
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=30)
    
    if result.returncode != 0:
        print(f"✗ ffprobe error (exit code {result.returncode})")
        print(f"stderr: {result.stderr}")
        # Try alternative command
        print("Trying alternative ffprobe command...")
        cmd2 = [FFPROBE_PATH, "-show_format", input_file]
        result = subprocess.run(cmd2, capture_output=True, text=True, check=False)
        if "duration" in result.stdout:
            for line in result.stdout.split("\n"):
                if "duration=" in line:
                    duration = int(float(line.split("=")[1]))
                    break
        else:
            exit(1)
    else:
        duration_str = result.stdout.strip()
        if duration_str:
            duration = int(float(duration_str))
        else:
            print("✗ Could not parse duration")
            exit(1)
    
    print(f"✓ Video duration: {duration} seconds ({duration//60} min {duration%60} sec)")
    
except subprocess.TimeoutExpired:
    print("✗ Timeout analyzing video")
    exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    exit(1)

print("")

# Calculate segments
num_segments = (duration + segment_length - 1) // segment_length
print(f"Segment length: {segment_length} seconds (2 minutes)")
print(f"Total segments to create: {num_segments}")
print("")
print("=" * 70)
print("CUTTING VIDEO INTO SEGMENTS")
print("=" * 70)
print("")

# Create segments
segment_count = 0
for i in range(num_segments):
    start_time = i * segment_length
    segment_num = i + 1
    output_file = os.path.join(output_dir, f"segment_{segment_num:03d}.mp4")
    
    end_time = min(start_time + segment_length, duration)
    
    print(f"[{segment_num:2d}/{num_segments}] segment_{segment_num:03d}.mp4")
    print(f"     Time: {start_time:4d}s - {end_time:4d}s")
    print(f"     Status: ", end="", flush=True)
    
    cmd = [
        FFMPEG_PATH,
        "-i", input_file,
        "-ss", str(start_time),
        "-t", str(segment_length),
        "-c:v", "libx264",
        "-c:a", "aac",
        "-q:v", "5",
        output_file,
        "-loglevel", "error",
        "-hide_banner"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        if os.path.exists(output_file):
            size_mb = os.path.getsize(output_file) / (1024*1024)
            print(f"✓ ({size_mb:.1f} MB)")
            segment_count += 1
        else:
            print(f"✗ Failed")
            if result.stderr:
                print(f"     Error: {result.stderr[:200]}")
    except subprocess.TimeoutExpired:
        print(f"✗ Timeout")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("")

print("=" * 70)
print("PROCESS COMPLETE")
print("=" * 70)
print(f"Segments created: {segment_count}/{num_segments}")
print(f"Output: {output_dir}")
print("")

# List created files
files = sorted(Path(output_dir).glob("segment_*.mp4"))
if files:
    print(f"Files created ({len(files)}):")
    total_size = 0
    for f in files:
        size_mb = f.stat().st_size / (1024*1024)
        total_size += size_mb
        print(f"  ✓ {f.name:20s} ({size_mb:7.1f} MB)")
    print(f"\n  Total: {total_size:.1f} MB")
    print("")
    print("✓ SUCCESS! All segments ready for training")
else:
    print("✗ No files were created")

print("=" * 70)
