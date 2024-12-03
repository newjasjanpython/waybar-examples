import subprocess
import re
import json
import time

def get_default_sink():
    result = subprocess.run(['pactl', 'get-default-sink'], capture_output=True, text=True)
    return result.stdout.strip()

def get_sink_volume(sink):
    result = subprocess.run(['pactl', 'get-sink-volume', sink], capture_output=True, text=True)
    match = re.search(r'front-left:\s*\d+\s*/\s*(\d+)%', result.stdout)
    if match:
        return int(match.group(1))
    return None

def output_json():
    sink = get_default_sink()
    volume = get_sink_volume(sink)
    data = {
        "text": f"{volume}%",
        "tooltip": f"Sink: {sink}",
        "class": "volume",
        "percentage": volume
    }
    print(json.dumps(data))
    print(end="", flush=True)

if __name__ == "__main__":
    output_json()
