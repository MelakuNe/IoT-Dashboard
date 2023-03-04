import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "sensor.csv")))


app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Temperature and Humidity Sensor Reading'),
                ],
            ),
        ],
    )


def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['time'][:50],
                    'y': df[' temperature'][:50],
                    'name': 'Temperature',
                    'marker': {'size': 12}
                },
                 {
                    'x': df['time'][:50],
                    'y': df['humidity'][:50],
                    'name': 'Humidity',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True, port=8050)
<<<<<<< HEAD
    
=======
>>>>>>> 3ca5d785153b4d1ca5e75e10dbc1c991d93b333d
