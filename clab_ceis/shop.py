from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import ceis_data  # Assuming ceis_data.py is available and correctly implemented
import plotly.graph_objects as go

# Initialize Dash App and CeisData
app = Dash(__name__, suppress_callback_exceptions=True)
data = ceis_data.CeisData()  # Initialize your CeisData instance



# Home Page Layout
def home_page():
    return html.Div(
        className="wrapper",
        children=[
            html.Header(
                html.H1("Welcome to Our Clothing Order Website", className="header-title"),
                className="card"
            ),
            html.Div(
                className="card",
                children=[
                    html.H2("Order a Dress or a Coat"),
                    html.P("Select the type of clothing you want to order:"),
                    html.Div(
                        className="order-form",
                        children=[
                            dcc.Link(
                                href="/dress",
                                children=html.Div(
                                    className="product",
                                    children=[
                                        html.Img(
                                            src=app.get_asset_url("dress.jpg"),
                                            alt="Dress",
                                            className="product-image"
                                        ),
                                        html.Span("Dress", className="product-label"),
                                    ],
                                ),
                            ),
                            dcc.Link(
                                href="/coat",
                                children=html.Div(
                                    className="product",
                                    children=[
                                        html.Img(
                                            src=app.get_asset_url("coat.jpg"),
                                            alt="Coat",
                                            className="product-image"
                                        ),
                                        html.Span("Coat", className="product-label"),
                                    ],
                                ),
                            ),
                        ],
                        style={"display": "flex", "gap": "20px"},
                    ),
                ],
            ),
            html.Footer(
                "© 2024 CeisShop. All rights reserved.",
                className="footer"
            ),
        ]
    )

# Dress Page Layout
def dress_page():
    return html.Div(
        className="product-detail",
        children=[
            html.H1("Dress", className="product-title"),
            html.Div(
                className="product-content",
                children=[
                    html.Div(
                        className="product-image",
                        children=html.Img(
                            src=app.get_asset_url("dress.jpg"),
                            alt="Dress",
                            style={"width": "100%", "border-radius": "8px"},
                        )
                    ),
                    html.Div(
                        className="product-description",
                        children=[
                            html.P(
                                "This is a beautiful dress, perfect for any occasion. "
                                "Made with high-quality materials, this dress will make you look stunning.",
                                style={"font-size": "18px"},
                            ),
                        ]
                    ),
                ],
                style={"display": "flex", "gap": "20px"},
            ),
            dcc.Link("Back to Home", href="/", className="back-link"),
        ],
    )

# Coat Page Layout
def coat_page():
    return html.Div(
        className="product-detail",
        children=[
            html.H1("Coat", className="product-title"),
            html.Div(
                className="product-content",
                children=[
                    html.Div(
                        className="product-image",
                        children=html.Img(
                            src=app.get_asset_url("coat.jpg"),
                            alt="Coat",
                            style={"width": "100%", "border-radius": "8px"},
                        )
                    ),
                    html.Div(
                        className="product-description",
                        children=[
                            html.P(
                                "This is a stylish coat, ideal for cold weather. "
                                "It combines elegance with comfort, ensuring you stay warm and look great.",
                                style={"font-size": "18px"},
                            ),
                        ]
                    ),
                ],
                style={"display": "flex", "gap": "20px"},
            ),
            dcc.Link("Back to Home", href="/", className="back-link"),
        ],
    )

# Dashboard Page Layout
# Dashboard Page Layout with Improved Alignment and Spacing
def dashboard_page():
    return html.Div(
        children=[
            
            
            # Resource Event Dashboard
            html.Div(
                children=[
                    html.H2("Resource Event Dashboard", style={"margin-bottom": "20px"}),
                    html.Button(
                        "Update DataTable", 
                        id="update-button", 
                        style={"margin-bottom": "20px"}
                    ),
                    dash_table.DataTable(
                        id="res-dashboard-table",
                        columns=[
                            {"name": col, "id": col} for col in data.get_data().columns  # Dynamically fetch columns
                        ],
                        style_table={
                            "overflowX": "auto",
                            "width": "100%",
                            "margin": "0 auto",
                        },
                        style_cell={
                            "textAlign": "left",
                            "padding": "5px",
                        },
                        style_header={
                            "backgroundColor": "rgb(230, 230, 230)",
                            "fontWeight": "bold",
                        },
                        page_size=5,
                    ),
                ],
                style={"margin-top": "40px", "padding": "20px"},
            ),
            # Circular Economy Dashboard
            html.Div(
                children=[
                    html.H2("Circular Economy Dashboard", style={"margin-bottom": "20px"}),
                    dash_table.DataTable(
                        id="circular-economy-table",
                        columns=[
                            {"name": "Metric", "id": "Metric"},
                            {"name": "Value", "id": "Value"},
                        ],
                        data=[
                            {"Metric": "Circular Economy Metric 1", "Value": 1234},
                            {"Metric": "Circular Economy Metric 2", "Value": 5678},
                            {"Metric": "Circular Economy Metric 3", "Value": 9012},
                        ],
                        style_table={
                            "overflowX": "auto",
                            "width": "50%",
                            "margin": "0 auto",
                        },
                        style_cell={
                            "textAlign": "left",
                            "padding": "5px",
                        },
                        style_header={
                            "backgroundColor": "rgb(230, 230, 230)",
                            "fontWeight": "bold",
                        },
                        page_size=3,
                    ),
                ],
                style={"margin-top": "40px", "padding": "20px"},
            ),
            dcc.Link("Back to Home", href="/", style={"display": "block", "margin-top": "30px", "text-align": "center"}),
        ],
        style={"max-width": "1200px", "margin": "0 auto", "padding": "20px"},  # Centralize entire content
    )


# Main Layout with Navigation Menu
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),  # Tracks the URL
        html.Div(
            className="menu",
            children=[
                dcc.Link("Home", href="/", className="menu-link", style={"margin-right": "20px"}),
                dcc.Link("Dashboard", href="/dashboard", className="menu-link", style={"margin-right": "20px"}),
                dcc.Link("Dress", href="/dress", className="menu-link", style={"margin-right": "20px"}),
                dcc.Link("Coat", href="/coat", className="menu-link"),
            ],
            style={
                "background-color": "#f5f5f5",
                "padding": "10px",
                "display": "flex",
                "justify-content": "center",
            },
        ),
        html.Div(id="page-content", style={"padding": "20px"}),  # Dynamic content area
    ]
)

# Callback to Render Pages Dynamically
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/dashboard":
        return dashboard_page()
    elif pathname == "/dress":
        return dress_page()
    elif pathname == "/coat":
        return coat_page()
    else:
        return home_page()

# Data Callbacks for Resource Event Dashboard
@app.callback(
    Output("res-dashboard-table", "data", allow_duplicate=True),
    Input("flow-chart", "tapEdgeData"),
    prevent_initial_call=True
)
def onTapEdge(tapEdgeData):
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
    [Input("update-button", "n_clicks")],
    prevent_initial_call=True
)
def update_table(n_clicks):
    return data.get_data().to_dict("records")

if __name__ == "__main__":
    app.run_server(debug=True)
