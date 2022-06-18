import json
from datetime import datetime
from pathlib import Path


def main():
    home = str(Path.home())
    findmy_cache = f"{home}/Library/Caches/com.apple.findmy.fmipcore/Items.data"

    with open(findmy_cache, "r") as f:
        data = json.load(f)

    for item in data:
        if item["name"] == "Dániel’s Backpack":
            timestamp = int(item["location"]["timeStamp"]) / 1000
            location = {
                "latitude": item["location"]["latitude"],
                "longitude": item["location"]["longitude"],
                "altitude": item["location"]["altitude"],
                "timestamp": datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                "emoji": item["role"]["emoji"],
            }
            print(location)


if __name__ == '__main__':
    main()
