from dash import html, dash_table
from dash.dependencies import Input, Output
from utils.sparql_queries import fetch_material, fetch_location

def register_callbacks(app):
    @app.callback(
        Output("dynamic-tables-container", "children"),
        Input("fetch-material-data", "n_clicks"),
        prevent_initial_call=True
    )
    def update_material_tables(n_clicks):
        try:
            material_data = fetch_material()
            grouped_data = {}
            for item in material_data:
                recipe_name = item['recipe']
                if recipe_name not in grouped_data:
                    grouped_data[recipe_name] = []
                grouped_data[recipe_name].append(item)

            tables = []
            for recipe, rows in grouped_data.items():
                table = dash_table.DataTable(
                    columns=[
                        {"name": "Fabric Block Design", "id": "fabricBlockDesign"},
                        {"name": "Required Amount", "id": "requiredAmount"},
                        {"name": "Available Amount", "id": "availableAmount"},
                        {"name": "Ready For Assembly", "id": "readyForAssembly"},
                    ],
                    data=rows,
                    style_table={"overflowX": "auto", "width": "100%", "margin-top": "20px"},
                    style_cell={"textAlign": "left", "padding": "5px"},
                    style_header={"backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
                    page_size=5,
                )
                tables.append(html.Div([html.H4(f"Recipe: {recipe}"), table]))

            return html.Div(tables)
        except Exception as e:
            print(f"Error updating material tables: {e}")
            return html.Div("Error fetching data.")

    @app.callback(
        Output("location-data-table", "data"),
        Input("fetch-location-data", "n_clicks"),
        prevent_initial_call=True
    )
    def update_location_table(n_clicks):
        try:
            data = fetch_location()
            return data
        except Exception as e:
            print(f"Error fetching location data: {e}")
            return []
