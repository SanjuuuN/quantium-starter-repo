from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1("My Dash App", id="header"),
    dcc.Graph(id="graph", figure={
        "data": [{"x": [1, 2, 3], "y": [3, 1, 2], "type": "bar"}]
    }),
    dcc.Dropdown(
        id="region-picker",
        options=[
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
        ],
        value="north",
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)
