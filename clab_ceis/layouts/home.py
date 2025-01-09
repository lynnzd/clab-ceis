from dash import html, dcc

def home_page():
    return html.Div(
        className="wrapper",
        children=[
            html.Header(html.H1("Welcome to Our Clothing Order Website", className="header-title"), className="card"),
            html.Div(
                className="card",
                children=[
                    html.H2("Order a Skirt or a Top"),
                    html.P("Select the type of clothing you want to order:"),
                    html.Div(
                        className="order-form",
                        children=[
                            dcc.Link(
                                href="/skirt",
                                children=html.Div(
                                    className="product",
                                    children=[
                                        html.Img(
                                            src="/assets/skirt.jpg",
                                            alt="Skirt",
                                            className="product-image"
                                        ),
                                        html.Span("Skirt", className="product-label"),
                                    ],
                                ),
                            ),
                            dcc.Link(
                                href="/top",
                                children=html.Div(
                                    className="product",
                                    children=[
                                        html.Img(
                                            src="/assets/top.jpg",
                                            alt="Top",
                                            className="product-image"
                                        ),
                                        html.Span("Top", className="product-label"),
                                    ],
                                ),
                            ),
                        ],
                        style={"display": "flex", "gap": "20px"},
                    ),
                ],
            ),
            html.Footer("© 2024 CeisShop. All rights reserved.", className="footer"),
        ]
    )
