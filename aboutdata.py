import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
nav = Navbar()

body = dbc.Container(
    [
       dbc. Row(
            [
                dbc.Col(
                    [
                    html.Center(html.H4("Adatok bemutatása",style={'font-family' : 'Times New Roman'})),
                    html.P(''' A verseny adathalmazának forrása a PatchCamelyont (PCam),amely két független adathalmaz kombinációja,
                        a Radbound Egyetemi Orvosi Központ és az Ultrechti Egyetemi Orvosi Központ által gyűjtött adatoké.  ''',
                        style={'text-align': 'justify', 'text-indent' : '10%', }),
                    html.P(''' Az adathalmaz 277 483 digitális patológia képet tartalmaz, amelyek 96x96 pixelesek. Az adatgyűjteményben 
                        220 025 kép tartozik a tanulási halmazhoz (train), illetve 57 458 a tesztelési halmazhoz (test), minden képhez hozzárendelődik egy azonosító, 
                        amely egyben a kép neve is.''',style={'text-align': 'justify', 'text-indent' : '10%', }),
                    html.P('''A tanulási halmazhoz kapcsolódik egy .csv fájl, amely tartalmazza minden kép azonosítóját és annak címkéjét.
                        A pozitív címkék (1), azt jelentik, hogy a kép 32x32 pixeles középső régiója legalább 1 pixelnyi tumort tartalmaz, az ezen
                        kívül eső részek nem befolyásolják a címkét, a negatív címkéknél (0) a belső régió nem tartalmaz rákos sejtet.
                        A tanítási halmaz 130 908 negatív címkéjű (0) és 89 117 pozitív címkéjű (1) adatot tartalmaz.  ''',
                        style={'text-align': 'justify', 'text-indent' : '10%', }),
                    html.Center(html.H5("A képek tulajdonságai")),
                    html.Table(
                            [
                                html.Tr(
                                [
                                    html.Th("Kiterjesztés"),
                                    html.Td("TIF (.tif)")
                                ],style = { 'background-color' : '#DCDCDC' }),
                                 html.Tr(
                                [
                                    html.Th("Méret"),
                                    html.Td("96 x 96")
                                ]),
                                html.Tr(
                                [
                                    html.Th("Színcsatornák"),
                                    html.Td("3")
                                ],style = {'background-color' : '#DCDCDC' }),
                                html.Tr(
                                [
                                    html.Th("Bit/csatorna"),
                                    html.Td("8")
                                ]),
                                html.Tr(
                                [
                                    html.Th("Adattípus"),
                                    html.Td("Unsigned char")
                                ],style = { 'background-color' : '#DCDCDC'}),
                                html.Tr(
                                [
                                    html.Th("Tömörítés"),
                                    html.Td("Jpeg")
                                ],),
                            ],
                            style={
                                'text-align' : 'center',
                                'overflow-x':'auto',
                                'borderRadius': '10px',
                                'textAlign': 'center',
                                'margin': 'auto',
                                'width' : '70%'
                                }
                    ),
                    html.Br(),
                    html.Br(),
                    html.Center(dbc.Button("Adatok elérése", color="secondary", href="https://www.kaggle.com/c/histopathologic-cancer-detection/data"))
                    ], md=5),
                 dbc.Col([ 
                    dcc.Graph(
                        figure={
                         "data": [{"type": "pie","labels": ["Negatív","Pozitív"],"values": [130908,89117]}],
                        "layout": {"title": "Pozitív és negatív címkéjű adatok eloszlása","height": 380},
                        }),
                    html.Div(html.Img(src='../assets/aboutdata.png', style={'width':'100%'}))
                ])
            ]),
    ],
className="mt-4",
)

def AboutData():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SANDSTONE])
app.title = "Histopathology cancer detection"

app.layout = AboutData()

if __name__ == "__main__":
    app.run_server()