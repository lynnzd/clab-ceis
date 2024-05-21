#!/usr/bin/env python
from dash import Dash, Input, Output

from clab_ceis import ceis_data


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
