import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import pandas as pd

# Sample data with regions
dates = pd.date_range(start='2021-01-01', end='2021-01-31')

regions = ['north', 'east', 'south', 'west']
data = []

for region in regions:
    sales = [100 + i*3 + (10 if i >= 14 else 0) + regions.index(region)*5 for i in range(len(dates))]
    df_region = pd.DataFrame({
        'Date': dates,
        'Sales': sales,
        'Region': region
    })
    data.append(df_region)

df = pd.concat(data)
df = df.sort_values('Date')

app = dash.Dash(__name__)

# Inline styles for header and layout
header_style = {
    'textAlign': 'center',
    'color': '#2c3e50',
    'font-family': 'Arial, sans-serif',
    'padding': '20px',
    'backgroundColor': '#ecf0f1',
    'borderRadius': '5px',
    'marginBottom': '20px'
}

radio_style = {
    'textAlign': 'center',
    'marginBottom': '30px',
    'fontWeight': 'bold',
    'color': '#34495e'
}

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser: Pink Morsel Price Impact", style=header_style),

    dcc.RadioItems(
        id='region-radio',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'marginRight': '15px', 'cursor': 'pointer'},
        style=radio_style
    ),

    dcc.Graph(id='sales-line-chart'),

    html.P(
        "The red dashed line marks the Pink Morsel price increase on January 15, 2021. "
        "Use the radio buttons above to filter sales data by region."
    )
])


@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    grouped = filtered_df.groupby('Date')['Sales'].sum().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=grouped['Date'],
        y=grouped['Sales'],
        mode='lines+markers',
        name='Sales'
    ))

    fig.add_shape(
        type="line",
        x0='2021-01-15',
        y0=grouped['Sales'].min(),
        x1='2021-01-15',
        y1=grouped['Sales'].max(),
        line=dict(color='red', dash='dash')
    )

    fig.update_layout(
        title='Daily Sales Over Time',
        xaxis_title='Date',
        yaxis_title='Sales',
        hovermode='x unified',
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#f8f9fa',
        font=dict(family='Arial, sans-serif', size=12, color='#2c3e50')
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
