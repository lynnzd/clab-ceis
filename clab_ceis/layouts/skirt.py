from dash import html, dash_table, dcc

def skirt_page():
    return html.Div(
        className="product-detail",
        children=[
            html.H1("Skirt", className="product-title"),
            html.Div(
                className="product-content",
                children=[
                    html.Div(
                        className="product-image",
                        children=html.Img(
                            src="/assets/skirt.jpg",
                            alt="Skirt",
                            style={"width": "100%", "border-radius": "8px"},
                        )
                    ),
                    html.Div(
                        className="product-description",
                        children=[
                            html.P(
                                "Wrapped Skirt made of double-sided fabric, in light blue and dark blue colors.",
                                style={"font-size": "18px"},
                            ),
                            html.Button("Fetch Skirt Data", id="fetch-skirt-data"),
                            dash_table.DataTable(
                                id="skirt-data-table",
                                columns=[
                                    {"name": "Recipe", "id": "recipe", "presentation": "markdown"},
                                    {"name": "Fabric Block Design", "id": "fabricBlockDesign"},
                                    {"name": "Required Amount", "id": "requiredAmount"},
                                ],
                                style_table={"overflowX": "auto", "width": "100%", "margin-top": "20px"},
                                style_cell={"textAlign": "left", "padding": "5px"},
                                style_header={"backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
                                page_size=5,
                            ),
                        ],
                    ),
                ],
                style={"display": "flex", "gap": "20px"},
            ),
            dcc.Link(
                "Back to Home",
                href="/",
                className="back-link",
                style={"margin-top": "20px", "display": "block", "text-align": "center"},
            ),
        ],
    )
