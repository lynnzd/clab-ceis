from pathlib import Path

import pandas as pd


class CeisData():
    _data = None

    def __init__(self) -> None:
        self._data = self._read_data()

    # @property comes with some downsides e.g. when serializing or subscripting. Hence not used
    def get_data(self) -> pd.DataFrame:
        return self._data
    
    def set_data(self, data):
        self._data = data

    def _read_data(self):
        # TODO: make this configurable
        csv_path = Path("ceis/resevents.csv")
        if csv_path.exists():
            return pd.read_csv(csv_path).sort_values(by="Timestamp")
        else:
            return pd.read_csv("resevents.csv").sort_values(by="Timestamp")


class CeisTrade():
    _quote = {
        "CI ID": "D",
        "CIType": "Coat",
        "CO2eq": 33,
        "DATE": "2024-02-23",
        "EventID": 6,
        "EventTrigger": "Deliver",
        "EventType": "Product",
        "FROM": "Production",
        "RequestType": "Order",
        "STATUS": "In Progress",
        "TO": "Use",
        "Timestamp": "2024-02-15T09:27:40"
    }
    _offer = {}

    # @property comes with some downsides e.g. when serializing or subscripting. Hence not used
    @staticmethod
    def get_quote():
        return CeisTrade._quote
    
    # @property comes with some downsides e.g. when serializing or subscripting. Hence not used
    @staticmethod
    def get_offer(data: CeisData):
        if not CeisTrade._offer:
            CeisTrade._offer = {
                "date": CeisTrade._quote["DATE"],
                "price": "25",
                "currency": "$",
                "co2eq": CeisTrade._quote["CO2eq"]
            }
        return CeisTrade._offer




# def _get_data():
#     csv_path = Path("clab_prototype/resevents.csv")
#     if csv_path.exists():
#         return pd.read_csv(csv_path).sort_values(by="Timestamp")
#     else:
#         return pd.read_csv("resevents.csv").sort_values(by="Timestamp")


# data = _get_data()


# ceis_event_tr = data["EventTrigger"].sort_values().unique()


