#!/usr/bin/env python

from enum import Enum

from dash import Dash, Input, Output, State, html, dash_table, dcc
import dash_cytoscape as cyto
from flask import request, jsonify
import pandas as pd

import ceis_data


class CeStages(Enum):
    Extraction = 1
    Production = 2
    Use = 3
    Waste = 4


class CeLoops(Enum):
    Repair = 11
    Remanufacture = 12
    Recycle = 13
    Composting = 14


CHART_HEIGHT=400
# ce_data = ceis_data.data

def get_callbacks(app: Dash, data: ceis_data.CeisData) -> None:

    @app.callback(
        Output("res-dashboard-table", "data", allow_duplicate=True),
        Input("flow-chart", "tapEdgeData"),
        prevent_initial_call=True
    )
    def onTapEdge(tapEdgeData):
        # global ce_data
        col_title = "EventTrigger"
        ce_data = data.get_data()
        filtered_data = ce_data[ce_data[col_title].str.contains(tapEdgeData["label"], case=False, na=False)]
        return filtered_data.to_dict("records")


    @app.callback(
            Output("res-dashboard-table", "data"),
            Input("flow-chart", "tapNodeData"),
            prevent_initial_call=True
    )
    def onTapNode(tapNodeData):
        col_title = "TO"
        ce_data = data.get_data()
        filtered_data = ce_data[ce_data[col_title].str.contains(tapNodeData["label"], case=False, na=False)]
        return filtered_data.to_dict("records")


    @app.callback(
        Output("res-dashboard-table", "data", allow_duplicate=True),
        [Input('update-button', 'n_clicks')],
        prevent_initial_call=True
    )
    def update_table(n_clicks):
        return data.get_data().to_dict('records')

# if __name__ == "__main__":
#     app.run_server(host="ceis", port="8051", debug=True)
