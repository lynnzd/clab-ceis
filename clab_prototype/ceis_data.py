import pandas as pd


data = (
    pd.read_csv("clab_prototype/resevents.csv")
    # pd.read_csv("resevents.csv")
    #.assign(ts=lambda data: pd.to_datetime(data["Timestamp"])) # , format="%Y-%m-%d"
    .sort_values(by="Timestamp")
)
ceis_event_tr = data["EventTrigger"].sort_values().unique()
