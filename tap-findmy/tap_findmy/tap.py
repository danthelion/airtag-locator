from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th

from tap_findmy.streams import (
    ItemStream,
)

STREAM_TYPES = [
    ItemStream,
]


class Tapfindmy(Tap):
    name = "tap-findmy"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "item_name",
            th.StringType,
            required=True,
            description="The name of the item to be tracked",
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
