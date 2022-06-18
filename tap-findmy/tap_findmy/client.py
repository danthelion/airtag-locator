import json
from datetime import datetime
from pathlib import Path
from typing import Optional, Iterable

from singer_sdk.streams import Stream


class FindMyStream(Stream):
    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        findmy_cache = f"{Path.home()}/Library/Caches/com.apple.findmy.fmipcore/Items.data"

        with open(findmy_cache, "r") as f:
            data = json.load(f)

        for item in data:
            if item["name"] == self.config["item_name"]:
                # Move timestamp to top level so we can use as PK
                ts = int(item["location"]["timeStamp"]) / 1000
                item["timestamp"] = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                yield item
