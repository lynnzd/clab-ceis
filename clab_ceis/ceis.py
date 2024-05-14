#!/usr/bin/env python

from enum import Enum

from dash import Dash, Input, Output, State, html, dash_table, dcc
import dash_cytoscape as cyto
from flask import request, jsonify
import pandas as pd

import ceis_data
import ceis_callbacks


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

# ce_data = ceis_data.CeisData()
# self._data.data = ce_data.data

class CeisMonitor():
    _model: pd.DataFrame = None
    _app: Dash = None
    _layout = None

    @property
    def layout(self):
        return self._layout
    
    def __init__(self, app) -> None:
        self._app = app
        self._model = ceis_data.CeisData()
        self.make_layout()
        self.get_route(self._app.server)
        ceis_callbacks.get_callbacks(self._app, self._model)
    
    def make_layout(self) -> None:
        # Sample flow chart data
        flow_chart_data = {
            "elements": [
                {"data": {"id": f"{CeStages.Extraction.value}", "label": f"{CeStages.Extraction.name}"}, "position": {"x": 100, "y": 0.5 * CHART_HEIGHT}},
                {"data": {"id": f"{CeStages.Production.value}", "label": f"{CeStages.Production.name}"}, "position": {"x": 300, "y": 0.5 * CHART_HEIGHT}},
                {"data": {"id": f"{CeStages.Use.value}", "label": f"{CeStages.Use.name}"}, "position": {"x": 500, "y": 0.5 * CHART_HEIGHT}},
                {"data": {"id": f"{CeStages.Waste.value}", "label": f"{CeStages.Waste.name}"}, "position": {"x": 700, "y": 0.5 * CHART_HEIGHT}},
                {"data": {"source": f"{CeStages.Extraction.value}", "target": f"{CeStages.Production.value}", "label": "Supply"}},
                {"data": {"source": f"{CeStages.Production.value}", "target": f"{CeStages.Use.value}", "label": "Deliver"}},
                {"data": {"source": f"{CeStages.Use.value}", "target": f"{CeStages.Waste.value}", "label": "Release"}},
                # loops
                {"data": {"id": f"{CeLoops.Repair.value}", "label": f"{CeLoops.Repair.name}", "source": f"{CeStages.Use.value}", "target": f"{CeStages.Use.value}"}},
                {"data": {"id": f"{CeLoops.Remanufacture.value}","label": f"{CeLoops.Remanufacture.name}", "source": f"{CeStages.Use.value}", "target": f"{CeStages.Production.value}"}},
                {"data": {"id": f"{CeLoops.Recycle.value}","label": f"{CeLoops.Recycle.name}", "source": f"{CeStages.Waste.value}", "target": f"{CeStages.Production.value}"}},
                {"data": {"id": f"{CeLoops.Composting.value}","label": f"{CeLoops.Composting.name}", "source": f"{CeStages.Waste.value}", "target": f"{CeStages.Extraction.value}"}},
            ]
        }

        self._layout = html.Div(
            children=[
                html.Header([
                    html.Div("Circular Lab Cockpit", className="logo")
                ]),
                html.Div([
                    html.H1("Product Lifecycle"),
                    # html.Div([
                    #     html.Img(
                    #         src=app.get_asset_url("lifecycle.png"),
                    #         alt="Product Lifecycle Placeholder",
                    #         style={"max-width": "100%", "height": "auto"}
                    #     )
                    # ], className="product-lifecycle"),
                    cyto.Cytoscape(
                        id="flow-chart",
                        layout={"name": "preset"},
                        style={"height": f"{CHART_HEIGHT}px"},
                        autolock=True,
                        elements=flow_chart_data["elements"],
                        panningEnabled=False,
                        zoom=1,
                        stylesheet=[
                            {
                                "selector": "node",
                                "style": {
                                    "label": "data(label)",
                                    "shape": "tag",
                                    # "width": f"{0.3 * CHART_HEIGHT}",
                                    # "height": f"{0.15 * CHART_HEIGHT}",
                                    "text-halign": "left",
                                    "text-valign": "bottom",
                                    "text-margin-x": "-10%",
                                    "line-color": "yellow",
                                    "background-color": "darkblue",
                                    "text-background-color": "grey",
                                    "text-background-opacity": 0.7,

                                },
                            },
                            {
                                "selector": "edge",
                                "style": {
                                    "label": "data(label)",
                                    "target-arrow-shape": "triangle",  # Set the arrow shape to triangle
                                    "arrow-scale": 1.5,
                                    "line-color": "darkblue",
                                    "text-margin-y" : "-15%",
                                },
                            },
                            {
                                "selector":  f"#{CeLoops.Repair.value}, #{CeLoops.Recycle.value}, #{CeLoops.Remanufacture.value}, #{CeLoops.Composting.value}",
                                "style": {
                                    "label": "data(label)",
                                    "curve-style": "unbundled-bezier",
                                    "control-point-distance": "200",
                                    "line-color": "orange",
                                    
                                },
                            },
                            {
                                "selector":  f"#{CeLoops.Composting.value}",
                                "style": {
                                    "label": "data(label)",
                                    "curve-style": "unbundled-bezier",
                                    "control-point-distance": "-300",
                                    "text-margin-y" : "15%",
                                },
                            },
                            {
                                "selector":  f"#{CeLoops.Remanufacture.value}",
                                "style": {
                                    "label": "data(label)",
                                    "curve-style": "unbundled-bezier",
                                    "control-point-distance": "-200",
                                    "text-margin-y" : "15%",
                                },
                            },
                        ],
                    ),
                    html.P(id="cytoscape-output"),

                    html.H1("Resource Event Dashboard"),
                    
                    html.Button('Update DataTable', id='update-button', n_clicks=0),

                    dash_table.DataTable(
                        id="res-dashboard-table",
                        columns=[{"name": col, "id": col} for col in self._model.get_data().columns],
                        data=self._model.get_data().to_dict("records"),
                        style_table={"maxWidth": f"{CHART_HEIGHT}px"},
                        style_cell={"textAlign": "center"},
                        style_header={"fontWeight": "bold"},
                    ),

                    html.H1("Circular Economy Dashboard"),
                    dash_table.DataTable(
                        id="dashboard-table",
                        columns=[
                            {"name": "Metric", "id": "metric"},
                            {"name": "Value", "id": "value"},
                        ],
                        data=[
                            {"metric": "Circular Economy Metric 1", "value": "1234"},
                            {"metric": "Circular Economy Metric 2", "value": "5678"},
                            {"metric": "Circular Economy Metric 3", "value": "9012"},
                        ],
                        style_table={"maxWidth": "600px"},
                        style_cell={"textAlign": "center"},
                        style_header={"fontWeight": "bold"},
                    ),

                ], className="wrapper")
            ]
        )
        self._app.layout = self._layout

    def get_route(self, server):
        @server.route('/quote', methods=['PUT'])
        def quote_endpoint():
            # Retrieve data from the HTTP request
            # global self._data.data
            data = request.json
            data["EventID"] = self._model.get_data().get("EventID").iloc()[-1] + 1
            self._model.set_data(pd.concat([self._model.get_data(), pd.DataFrame([data])], ignore_index=True))

            return jsonify(ceis_data.CeisTrade.get_offer(self._model.get_data()))


if __name__ == "__main__":
    app = Dash(
        __name__,
        # needed when callbacks and app are specified in different modules
        suppress_callback_exceptions=True
    )
    mon = CeisMonitor(app)
    # TODO: implement a good way to change the configuration
    # app.run_server(host="ceis", port="8051", debug=True)
    app.run_server(host="localhost", port="8051", debug=True)
