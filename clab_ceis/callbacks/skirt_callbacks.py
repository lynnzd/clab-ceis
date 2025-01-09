from dash.dependencies import Input, Output
from utils.sparql_queries import fetch_skirt_recipes

def register_callbacks(app):
    @app.callback(
        Output("skirt-data-table", "data"),
        Input("fetch-skirt-data", "n_clicks"),
        prevent_initial_call=True
    )
    def update_skirt_table(n_clicks):
        try:
            data = fetch_skirt_recipes()
            return data
        except Exception as e:
            print(f"Error fetching SPARQL data: {e}")
            return []
