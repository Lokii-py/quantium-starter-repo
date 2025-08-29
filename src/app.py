from dash import Dash, html, dcc, Input, Output,  callback
import pandas as pd
import plotly.express as px

#Data Preperation
df = pd.read_csv("pink_morsel_sales_summary.csv")
df['date'] = pd.to_datetime(df['date']) #Convert the string date into int datetime
df = df.sort_values(by='date')

total_sales = df['sales'].sum()
avg_daily_sales = df.groupby('date')['sales'].sum().mean()
last_day_sales = df.groupby('date')['sales'].sum().iloc[-1]

#Intialize the app
external_stylesheets = ['https://fonts.googleapis.com/css2?family=Lato&display=swap']
app = Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#1a1a2e',
    'text': '#EAEAEA',
    'chart_line': '#0074D9',
    'accent': '#FF851B'
}

card_style = {
    'padding': '20px',
    'margin': '10px',
    'backgroundColor': '#1E1E1E',
    'borderRadius': '5px',
    'textAlign': 'center',
    'flex': 1
}

#App component
app.layout = html.Div(style={"backgroundColor" : colors['background'], 'color': colors['text'], 'fontFamily': 'lato, sans-serif'} ,children=[

    html.H1(
        children = "Soul Foods: Pink Morsel Sales Summary DashBoard",
        style = {
            "textAlign": "center",
            'paddingTop': '20px',
            "color": colors["accent"]
        }
    ),

    html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}, children = [

        html.Div(style=card_style, children=[
            html.H3(f'${total_sales:,.0f}'),
            html.P("Total Sales")
        ]),

        html.Div(style=card_style, children=[
            html.H3(f'${avg_daily_sales:,.0f}'),
            html.P("Average Daily Sales")
        ]),

        html.Div(style=card_style, children=[
            html.H3(f'${last_day_sales:,.0f}'),
            html.P("Most Recent Day's Sales")
        ]),
    ]),


    html.Div(style={'width': "80%", 'margin': '0 auto', 'textAlign': 'center', 'padding': '10px', 'fontSize': '20px'}, children=[
        html.H4("Choose a Region"),
        dcc.RadioItems(
            id='region',
            options=[{'label': region, 'value': region} for region in ['all'] + list(df['region'].unique())],
            value='all',
            inline=True,
            labelStyle={'marginRight': '30px'}
        )
    ]),

    html.Div(style={'padding': '10px'}, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

@callback(
    Output('sales-line-chart', 'figure'),
    Input('region', 'value'))

def update_graph(selected_region):
    if selected_region == 'all':
        data_to_plot = df
    else:
        data_to_plot = df[df["region"] == selected_region]

    fig = px.line(
        data_to_plot,
        x = 'date',
        y = 'sales',
        title = 'Pink Morsel Sales Over Time'
    )

    fig.add_vline(x='2021-01-15', line_width=3, line_dash='dash', line_color=colors['accent'])

    fig.update_traces(line_color=colors['chart_line'])

    fig.update_layout(
        transition_duration=500,
        plot_bgcolor=colors['background'],
        paper_bgcolor='#1E1E1E',
        font_color=colors['text']
    )

    return fig

#Run the app
if __name__ == "__main__":
    app.run(debug = True)