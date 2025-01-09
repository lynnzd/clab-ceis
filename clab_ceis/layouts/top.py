from dash import html, dash_table, dcc

def top_page():
    return html.Div(
        className="product-detail",
        children=[
            html.H1("Top", className="product-title"),
            html.Div(
                className="product-content",
                children=[
                    html.Div(
                        className="product-image",
                        children=html.Img(
                            src="/assets/top.jpg",
                            alt="Top",
                            style={"width": "100%", "border-radius": "8px"},
                        )
                    ),
                    html.Div(
                        className="product-description",
                        children=[
                            html.P(
                                "Crop top made from fine hemp fabric in a linen weave." 
                                "Loose fit with a T-shape geometric opening at the neck.",
                                style={"font-size": "18px"},
                            ),
                             # Button to trigger SPARQL query
                            html.Button("Fetch Top Data", id="fetch-top-data"),
                            # DataTable to display SPARQL results
                            dash_table.DataTable(
                                id="top-data-table",
                                columns=[
                                    {"name": "Recipe", "id": "recipe"}
                                ],
                                style_table={
                                    "overflowX": "auto",
                                    "width": "100%",
                                    "margin-top": "20px",
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
                        ]
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
