from dash.dependencies import Input, Output
from utils.sparql_queries import fetch_top_recipes

def register_callbacks(app):
    @app.callback(
        Output("top-data-table", "data"),
        Input("fetch-top-data", "n_clicks"),
        prevent_initial_call=True
    )
    def update_top_table(n_clicks):
        try:
            data = fetch_top_recipes()
            return data
        except Exception as e:
            print(f"Error fetching SPARQL data: {e}")
            return []
