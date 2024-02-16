#!/usr/bin/env python


import copy

from dash import Dash, dcc, html, Input, Output, State
import httpx

from ceis_data import quote

app = Dash(__name__)
server = app.server

app.layout = html.Div([
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
                        src=app.get_asset_url("dress.jpg"),
                        alt="Dress",
                        className="product-image",
                    ),
                    html.Img(
                        src=app.get_asset_url("coat.jpg"),
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

@app.callback(
    Output("quote-result", "children"),
    Input("btn-get-quote", "n_clicks"),
    State("clothing-type", "value"),
    prevent_initial_call=True
)
def display_quote(n_clicks, value):
    quote_url = "http://ceis:8051/quote"
    headers = {"Content-Type": "application/json"}
    product_quote = copy.deepcopy(quote)
    product_quote["CIType"] = value
    if n_clicks > 0:
        response = httpx.put(quote_url, json=product_quote, headers=headers).json()
        return f"We can offer you the {value} for {response["price"]}{response["currency"]}, on the {response["date"]}, causing {response["co2eq"]} kg CO2eq"
    else:
        return ""

if __name__ == "__main__":
    app.run_server(host="shop", debug=True)