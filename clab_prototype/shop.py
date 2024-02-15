#!/usr/bin/env python


from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Header(
        html.H1(
            "Welcome to Our Clothing Order Website",
            style={'color': '#fff', 'background-color': '#333', 'padding': '20px', 'text-align': 'center'}),
    ),
    html.Div(
        className='container',
        children=[
            html.H2("Order a Dress or a Coat"),
            html.P("Select the type of clothing you want to order:"),
            html.Div(
                className='order-form',
                children=[
                    html.Img(
                        src=app.get_asset_url("dress.jpg"),
                        alt="Dress",
                        className="product-image",
                    ),
                    html.Img(
                        src=app.get_asset_url("coat.jpg"),
                        alt="Coat",
                        className="product-image",
                    ),
                    dcc.Dropdown(
                        id='clothing-type',
                        options=[
                            {'label': 'Dress', 'value': 'dress'},
                            {'label': 'Coat', 'value': 'coat'}
                        ],
                        value='dress',
                        style={'flex': '1'},
                    ),
                    # html.Br(),
                    # html.Br(),
                    html.Button("Get Quote", id="btn-get-quote", n_clicks=0),
                    html.Div(id="quote-result", className="quote-result", style={'font-size': '18px', 'margin-top': '20px', 'color': '#333'}),
                ]
            ),
        ]
    ),
])

@app.callback(
    Output('quote-result', 'children'),
    Input('btn-get-quote', 'n_clicks')
)
def display_quote(n_clicks):
    if n_clicks > 0:
        return "25$, 40 kg CO2eq"
    else:
        return ""

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)