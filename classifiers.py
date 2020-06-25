import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd



from navbar import Navbar
nav = Navbar()

body = dbc.Container(
    [
        dbc.Col(
            [
                html.Center(html.H2('Osztályozók összehasonlítása',style={'font-family' : 'Times New Roman'})),
                html.Br(),
                html.Br(),
            ]
        ),
        dbc.Row(
           [
                dbc.Col(
                   [
                        html.Center(html.H4("Pablo Gómez és csapatának megvalósítása",style={'font-family' : 'Times New Roman'})),
                        html.Br(),
                        html.Br(),
                   ]
                ),
                dbc.Col(
                   [
                        html.Center(html.H4("Marsh modellje ",style={'font-family' : 'Times New Roman'})),
                        html.Br(),
                        html.Br(),
                   ]
               ),
           ]
       ),
       dbc.Col(
           [
               html.Center(html.H4('Tanítási paramérterek')), 
               html.Br(), 
               html.Br()
        ]),
       dbc.Row(
           [
               dbc.Col(
                   [
                       html.Center(html.Table(
                           [
                               html.Tr(
                                        [
                                            html.Th("Epochok száma:"),
                                            html.Td("8")
                                        ],style = { 'background-color' : '#DCDCDC'}
                                ),
                                html.Tr(
                                        [
                                            html.Th("Batch mérete:"),
                                            html.Td("32")
                                        ]
                                ),
                                html.Tr(
                                        [
                                            html.Th("Veszteségfüggvény:"),
                                            html.Td("Bináris kersztentrópia")
                                        ],style = { 'background-color' : '#DCDCDC'}
                                 ),
                                 html.Tr(
                                        [
                                            html.Th("Optimalizáló:"),
                                            html.Td("Adam")
                                        ]
                                 ),
                                 html.Tr(
                                        [
                                            html.Th("Tanulási ráta:"),
                                            html.Td("0,01")
                                        ],style = { 'background-color' : '#DCDCDC'}
                                 )
                           ], style = {'text-align' : 'center',
                           'overflow-x':'auto',
                                    'borderRadius': '10px',
                                    'textAlign': 'center',
                                    'margin': 'auto',
                                    'width' : '70%',
                                    'border' : '1px solid'}
                       ))
                   ]
               ),
               dbc.Col(
                   [
                       html.Table(
                           [
                               html.Tr(
                                        [
                                            html.Th("Epochok száma"),
                                            html.Td("20")
                                        ],
                                        style = { 'background-color' : '#DCDCDC'}
                                ),
                                html.Tr(
                                        [
                                            html.Th("Batch mérete"),
                                            html.Td("10")
                                        ]
                                ),
                                html.Tr(
                                        [
                                            html.Th("Veszteségfüggvény"),
                                            html.Td("Bináris kersztentrópia")
                                        ],
                                        style = { 'background-color' : '#DCDCDC'}
                                 ),
                                 html.Tr(
                                        [
                                            html.Th("Optimalizáló"),
                                            html.Td("Adam")
                                        ]
                                 ),
                                 html.Tr(
                                        [
                                            html.Th("Tanulási ráta"),
                                            html.Td("0,00015")
                                        ],
                                        style = { 'background-color' : '#DCDCDC'}
                                 )
                           ],
                           style = {
                                    'text-align' : 'center',
                                    'overflow-x':'auto',
                                    'borderRadius': '10px',
                                    'textAlign': 'center',
                                    'margin': 'auto',
                                    'width' : '70%',
                                    'border' : '1px solid'
                                   }
                       )]
               )]
            ),
             dbc.Col(
                 [
                    html.Br(),
                    html.Br(),
                    html.Center(html.H4('A veszteség alakulása a tanítás és érvényesítés alatt',style={'font-family' : 'Times New Roman'})),
                 ]
             ),
            dbc.Row(
                [
                    dbc.Col(
                    [
                       html.Center(dcc.Graph(
                         figure={"data": [
                          {"x": [1,2,3,4,5,6,7,8],"y": [0.6565,0.5012,0.2691,0.2321,0.2099,0.2562,0.1864,0.1799], 'type':'scatter', 'name':'Tanítási veszteség'  },
                          {"x": [1,2,3,4,5,6,7,8],"y": [0.6483,0.5290,0.2866,0.2327,0.2131,0.3857,0.1927,0.1994],'type':'scatter', 'name':'Validációs veszteség' }],
                          'layout': {
                        'title': 'Veszteség ábrázolása',
                        'xaxis': dict(
                            title = 'Epoch',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'yaxis': dict(
                            title = 'Veszteség',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'width':'80%'
                    }}
                        )),
                   ]
               ),
                    dbc.Col(
                    [
                       html.Center(dcc.Graph(
                         figure={"data": [
                          {"x": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],"y": [0.4282,0.3326,0.2916,0.2469,0.2466,0.2315,0.2206,0.1893,0.1811,0.1742,
                          0.1697,0.1526,0.1470,0.1446,0.1417,0.1388,0.1365,0.1253,0.1240,0.1217], 'type':'scatter', 'name':'Tanítási veszteség'  },
                          {"x": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],"y": [0.3671,0.3087,0.2789,0.2457,0.2207,0.2395,0.2197,0.1906,0.1783,0.1820,
                          0.1956,0.1678,0.1636,0.1626,0.1653,0.1670,0.1648,0.1713,0.1580,0.1581],'type':'scatter', 'name':'Validációs veszteség' }],
                          'layout': {
                        'title': 'Veszteség ábrázolása',
                        'xaxis': dict(
                            title = 'Epoch',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'yaxis': dict(
                            title = 'Veszteség',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'width':'80%'
                    }
                        }
                        )),
                    ]
               )]
       ),
             dbc.Col(
                [
                    html.Br(),
                    html.Br(),
                    html.Center(html.H4('A pontosság alakulása a tanítás és érvényesítés alatt',style={'font-family' : 'Times New Roman'}))
                ]),
            dbc.Row(
                [
                dbc.Col(
                   [
                        html.Center(dcc.Graph(
                        figure={"data": [
                          {"x": [1,2,3,4,5,6,7,8],"y": [0.7625,0.7895,0.8892,0.9011,0.9362,0.8996,0.9325,0.9271], 'type':'scatter', 'name':'Tanítási pontosság'  },
                          {"x": [1,2,3,4,5,6,7,8],"y": [0.7709,0.7754,0.8752,0.9088,0.9151,0.8493,0.9273,0.9119],'type':'scatter', 'name':'Validációs pontosság' }],
                          'layout': {
                        'title': 'Pontosság ábrázolása',
                        'xaxis': dict(
                            title = 'Epoch',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'yaxis': dict(
                            title = 'Pontosság',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'width':'80%'
                    }}
                        )),
                   ]
                ),
                dbc.Col(
                   [
                        html.Center(dcc.Graph(
                        figure={"data": [
                          {"x": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],"y": [0.8066,0.8567,0.8775,0.8909,0.9006,0.9078,0.9125,0.9270,0.9302,0.9332,
                          0.9343,0.9423,0.9441,0.9449,0.9462,0.9476,0.9487,0.9530,0.9537,0.9540], 'type':'scatter', 'name':'Tanítási pontosság'  },
                          {"x": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],"y": [0.8353,0.8651,0.8823,0.8989,0.9141,0.9041,0.9107,0.9268,0.9317,0.9313,
                          0.9249,0.9367,0.9391,0.9401,0.9402,0.9384,0.9381,0.9362,0.9430,0.9432],'type':'scatter', 'name':'Validációs pontosság' }],
                          'layout': {
                        'title': 'Pontosság ábrázolása',
                        'xaxis': dict(
                            title = 'Epoch',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'yaxis': dict(
                            title = 'Pontosság',
                            titlefont = dict(
                                family = 'Helvetica, monospace',
                                size = 12,
                                color = '#7f7f7f'
                            )
                        ),
                        'width':'80%'
                    }
                        }))
                   ]),
           ]),
       dbc.Col(
           [
               html.Center(html.H4('A ROC görbe alakulása és az AUC értéke',style={'font-family' : 'Times New Roman'})),
               
           ]
       ),
       dbc.Row(
           [
               dbc.Col(
                   [
                       html.Center(html.Div(html.Img(src='../assets/ROC1.png', style={'width':'90%'})))
                   ]
               ),
               dbc.Col(
                   [
                      html.Center(html.Div(html.Img(src='../assets/ROC2.png', style={'width':'90%'})))
                   ]
               )
           ]
       ),
       dbc.Col(
           [
               html.Br(),
               html.Br(),
               html.Center(html.H4('Konfúziós mátrix',style={'font-family' : 'Times New Roman'} )),
               html.Br(),
          
           ]
       ),
       dbc.Row(
           [
               dbc.Col(
                   [
                       html.Center(html.Table(
                           [
                                html.Tr(
                                   [
                                       html.Th(" ", style = {'border' : '1px solid'}),
                                       html.Th('Valós 1 - Pozitív', style = {'border' : '1px solid'}),
                                       html.Th('Valós 0 - Negatív', style = { 'border' : '1px solid'}),
                                    ]),
                                html.Tr(
                                   [
                                       html.Th('Jósolt 1 - Pozitív', style = {'border' : '1px solid'}),
                                       html.Td('7 735', style = {'border' : '1px solid'}),
                                       html.Td('265', style = {'border' : '1px solid'}),
                                   ]),
                                html.Tr(
                                    [
                                        html.Th('Jósolt 0 - Negatív', style = {'border' : '1px solid'}),
                                        html.Td('1 269', style = {'border' : '1px solid'}),
                                        html.Td('6 731', style = {'border' : '1px solid' }),
                                    ] 
                               )
                           ], style = {
                               'border' : '1px solid',
                               'text-align' : 'center',
                               'height' : '200px',
                               'width' : '80%',
                               'font-size' : '1.5em',
                               'background-color' : '#F8F5F0'

                           }
                       ))
                   ]
               ),
                dbc.Col(
                   [
                       html.Center(html.Table(
                           [
                                html.Tr(
                                   [
                                       html.Th(" ", style = {'border' : '1px solid'}),
                                       html.Th('Valós 1 - Pozitív', style = {'border' : '1px solid'}),
                                       html.Th('Valós 0 - Negatív', style = { 'border' : '1px solid'}),
                                    ]),
                                html.Tr(
                                   [
                                       html.Th('Jósolt 1 - Pozitív', style = {'border' : '1px solid'}),
                                       html.Td('7 541', style = {'border' : '1px solid'}),
                                       html.Td('459', style = {'border' : '1px solid'}),
                                   ]),
                                html.Tr(
                                    [
                                        html.Th('Jósolt 0 - Negatív', style = {'border' : '1px solid'}),
                                        html.Td('450', style = {'border' : '1px solid'}),
                                        html.Td('7 550', style = {'border' : '1px solid' }),
                                    ] 
                               )
                           ], style = {
                               'border' : '1px solid',
                               'text-align' : 'center',
                               'height' : '200px',
                               'width' : '80%',
                               'font-size' : '1.5em',
                               'background-color' : '#F8F5F0'

                           }
                       ))
                   ]
               )
           ]

       ),
       dbc.Row(
           [
               dbc.Col(
                   [
                       html.Br(),
                       html.Center(html.A("Az osztályozó leírása itt érhető el", href='https://www.kaggle.com/gomezp/complete-beginner-s-guide-eda-keras-lb-0-93', style = {'color':'orange', 'font-weight':'bold'}
                       )),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                   ]
               ),
               dbc.Col(
                   [
                       html.Br(),
                       html.Center(html.A("Az osztályozó leírása itt érhető el", href='https://www.kaggle.com/vbookshelf/cnn-how-to-use-160-000-images-without-crashing', style = {'color':'orange', 'font-weight':'bold'}))
                   ]
               )
           ]
       )
    ],
className="mt-4",
)

def Classifiers():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.title = "Histopathology cancer detection"
app.layout = Classifiers()
if __name__ == "__main__":
    app.run_server()