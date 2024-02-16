from pathlib import Path

import pandas as pd


def _get_data():
    csv_path = Path("clab_prototype/resevents.csv")
    if csv_path.exists():
        return pd.read_csv(csv_path).sort_values(by="Timestamp")
    else:
        return pd.read_csv("resevents.csv").sort_values(by="Timestamp")


data = _get_data()


ceis_event_tr = data["EventTrigger"].sort_values().unique()


quote = {
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

offer = {
    "date": quote["DATE"],
    "price": "25",
    "currency": "$",
    "co2eq": quote["CO2eq"]
}