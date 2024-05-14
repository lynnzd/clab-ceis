#!/usr/bin/env python
from dash import Dash, dcc, html

from clab_ceis import shop_callbacks


class CeisShop():
    _app: Dash = None
    _layout = None

    @property
    def layout(self):
        return self._layout
    
    def __init__(self, app) -> None:
        self._app = app
        # self._model = ceis_data.CeisData()
        self.make_layout()
        # self.get_route(self._app.server)
        shop_callbacks.get_callbacks(self._app)

    def make_layout(self):
        self._layout = html.Div([
            html.Header(
                html.H1(
                    "Welcome to Our Clothing Order Website",
                    style={"color": "#fff", "background-color": "#333", "padding": "20px", "text-align": "center"}),
            ),
            html.Div(
                className="container",
                children=[
                    html.H2("Order a Dress or a Coat"),
                    html.P("Select the type of clothing you want to order:"),
                    html.Div(
                        className="order-form",
                        children=[
                            html.Img(
                                src=self._app.get_asset_url("dress.jpg"),
                                alt="Dress",
                                className="product-image",
                            ),
                            html.Img(
                                src=self._app.get_asset_url("coat.jpg"),
                                alt="Coat",
                                className="product-image",
                            ),
                            dcc.Dropdown(
                                id="clothing-type",
                                options=[
                                    {"label": "Dress", "value": "Dress"},
                                    {"label": "Coat", "value": "Coat"}
                                ],
                                value="dress",
                                style={"flex": "1"},
                            ),
                            # html.Br(),
                            # html.Br(),
                            html.Button("Get Quote", id="btn-get-quote", n_clicks=0),
                            html.Div(id="quote-result", className="quote-result", style={"font-size": "18px", "margin-top": "20px", "color": "#333"}),
                        ]
                    ),
                ]
            ),
        ])

        self._app.layout = self._layout

if __name__ == "__main__":
    app = Dash(__name__)
    shop = CeisShop(app)

    app.run_server(host="localhost", debug=True)
    # app.run_server(host="shop", debug=True)