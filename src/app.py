from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

#Intialize the data
df = pd.read_csv("pink_morsel_sales_summary.csv")

#Convert the string date into int datetime
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

#Intialize the app
app = Dash(__name__)

#Fig
fig = px.line(df, x = 'date', y = 'sales', title = 'Pink Morsel Sales Over Time')

fig.add_vline(x='2021-01-15', line_width=3, line_dash='dash', line_color='red')

#App component
app.layout = html.Div(children=[
    html.H1(
        children = "Soul Foods: Pink Morsel Sales Summary",
        style = {"textalign": "center"}
    ),

    html.Hr(),

    dcc.Graph(
        id = 'Sales Line Char',
        figure = fig
    )

])

#Run the app
if __name__ == "__main__":
    app.run(debug = True)