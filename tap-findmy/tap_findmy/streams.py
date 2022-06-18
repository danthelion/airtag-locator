from singer_sdk import typing as th

from tap_findmy.client import FindMyStream


class ItemStream(FindMyStream):
    name = "Item"
    primary_keys = ["name", "timestamp"]
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("location", th.ObjectType(
            th.Property("longitude", th.NumberType()),
            th.Property("latitude", th.NumberType()),
            th.Property("altitude", th.NumberType()),
            th.Property("timeStamp", th.NumberType()),
        )),
        th.Property("role", th.ObjectType(
            th.Property("name", th.StringType()),
            th.Property("emoji", th.StringType()),
            th.Property("identifier", th.NumberType()),
        )),
        th.Property("timestamp", th.DateTimeType),
    ).to_dict()
