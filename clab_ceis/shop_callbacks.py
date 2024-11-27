import copy

import httpx
from dash.dependencies import (
    Input,
    Output,
    State
)

import ceis_data as cd
import config

def get_callbacks(app):

    @app.callback(
        Output("quote-result", "children"),
        Input("btn-get-quote", "n_clicks"),
        State("clothing-type", "value"),
        prevent_initial_call=True
    )
    def display_quote(n_clicks, value):
        quote_url = f"http://{config.CEIS_MONITOR_HOSTNAME}:{config.CEIS_MONITOR_PORT}/quote"
        headers = {"Content-Type": "application/json"}
        product_quote = copy.deepcopy(cd.CeisTrade.get_quote())
        product_quote["CIType"] = value
        if n_clicks > 0:
            response = httpx.put(quote_url, json=product_quote, headers=headers).json()
            return f"We can offer you the {value} for {response["price"]}{response["currency"]}, on the {response["date"]}, causing {response["co2eq"]} kg CO2eq"
        else:
            return ""