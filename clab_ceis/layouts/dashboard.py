from dash import html, dash_table

def dashboard_page():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.P("Material Available", style={"font-size": "30px"}),
                    html.Button("Fetch Material Data", id="fetch-material-data"),
                    html.Div(id="dynamic-tables-container", style={"margin-top": "30px"}),    
                ]
            ),
            html.Div(
                children=[
                    html.P("Fabric Blocks", style={"font-size": "30px"}),
                    html.Button("Fetch Location Data", id="fetch-location-data"),
                    dash_table.DataTable(
                        id="location-data-table",
                        columns=[
                            {"name": "Location", "id": "location"},
                            {"name": "Fabric Block Design", "id": "fabricBlockDesign"},
                            {"name": "Count At Location", "id": "countAtLocation"},
                        ],
                        style_table={"overflowX": "auto", "width": "100%", "margin-top": "20px"},
                        style_cell={"textAlign": "left", "padding": "5px"},
                        style_header={"backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
                        page_size=5,
                    ),
                ]
            ),
            html.Div(style={"max-width": "1200px", "margin": "0 auto", "padding": "20px"}),  # Center content
        ]
    )
