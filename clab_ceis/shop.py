from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Initialize Dash App
app = Dash(__name__)

# Home Layout with Clickable Divs
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

# Layout for the Dress Page
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

# Layout for the Coat Page
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

# Main Layout with Dynamic Routing
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
    ]
)

# Callback to Render Pages
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/dress":
        return dress_page()
    elif pathname == "/coat":
        return coat_page()
    else:
        return home_page()  # This will now be correctly recognized.

if __name__ == "__main__":
    app.run_server(debug=True)
