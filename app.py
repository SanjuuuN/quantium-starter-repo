import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Sample data generation for illustration; replace this with your actual data loading
data = {
    'Date': pd.date_range(start='2021-01-01', end='2021-01-31'),
    'Sales': [100 + (i * 3) + (10 if i >= 14 else 0) for i in range(31)]  # Sales increase after Jan 15
}
df = pd.DataFrame(data)

# Sort by Date (just in case)
df = df.sort_values('Date')

app = dash.Dash(__name__)

app.layout = html.Div([
    # Header
    html.H1("Soul Foods Sales Visualiser: Pink Morsel Price Impact"),

    # Line Chart
    dcc.Graph(
        id='sales-line-chart',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Sales'],
                    mode='lines+markers',
                    name='Sales'
                ),
                # Add vertical line on Jan 15, 2021 to mark price increase
                go.Scatter(
                    x=[pd.Timestamp('2021-01-15'), pd.Timestamp('2021-01-15')],
                    y=[df['Sales'].min(), df['Sales'].max()],
                    mode='lines',
                    line=dict(color='red', dash='dash'),
                    name='Price Increase (Jan 15, 2021)'
                )
            ],
            'layout': go.Layout(
                title='Daily Sales Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Sales'},
                hovermode='closest'
            )
        }
    ),

    # Optional explanatory note
    html.P("The red dashed line marks the Pink Morsel price increase on January 15, 2021. "
           "Observe sales trends before and after this date to answer the business question.")
])

if __name__ == '__main__':
    app.run(debug=True)
