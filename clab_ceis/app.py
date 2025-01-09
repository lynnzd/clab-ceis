from dash import Dash, dcc, html
from layouts.home import home_page
from layouts.skirt import skirt_page
from layouts.top import top_page
from layouts.dashboard import dashboard_page
from callbacks import skirt_callbacks, top_callbacks, dashboard_callbacks
from dash.dependencies import Input, Output

# Initialize the app
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Define app layout
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(
            className="menu",
            children=[
                dcc.Link("Home", href="/", className="menu-link", style={"margin-right": "20px"}),
                dcc.Link("Dashboard", href="/dashboard", className="menu-link", style={"margin-right": "20px"}),
            ],
            style={
                "background-color": "#f5f5f5",
                "padding": "10px",
                "display": "flex",
                "justify-content": "center",
            },
        ),
        html.Div(id="page-content", style={"padding": "20px"}),
    ]
)

# Page routing callback
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/dashboard":
        return dashboard_page()
    elif pathname == "/skirt":
        return skirt_page()
    elif pathname == "/top":
        return top_page()
    else:
        return home_page()

# Import callbacks
skirt_callbacks.register_callbacks(app)
top_callbacks.register_callbacks(app)
dashboard_callbacks.register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
