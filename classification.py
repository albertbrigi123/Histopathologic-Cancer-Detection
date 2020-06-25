
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import datetime
import numpy as np


from dash.dependencies import Input, Output, State

from navbar import Navbar
nav = Navbar()

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SANDSTONE])

body = dbc.Container(
    [
        dbc.Col(
        [
            html.Center(html.H3("Képosztályozás",style={'font-family' : 'Times New Roman'})),
            html.Br(),
            html.Div([
                dcc.Upload(
                    id='upload-image',
                    children=html.Div([
                        'Kép behúzása ide, vagy ',
                         html.A('Kép kiválasztása'), 
                         html.Br(),
                         '.png vagy .jpg formátumban'
                    ]),
                    style={
                        'width': '50%',
                        'height': '100px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': 'auto'
                    },
                    multiple=True)]),
            html.Br(),
            html.Br(),
            html.Div(id = 'output-image-upload'),
            html.Br(),
            html.Br(),
           
            html.Br(),
        ]) 
    ],
className="mt-4",
)




def Classification():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app.title = "Histopathology cancer detection"

app.layout = Classification()



if __name__ == "__main__":
    app.run_server()