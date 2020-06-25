import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
nav = Navbar()

body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.Center(html.H2("Weboldal célja",style={'font-family' : 'Times New Roman'})),
                     html.Br(),
                     html.Br(),
                     html.P(
                         """A rákkutatás is óriási fejlődéseken ment keresztül, mivel egyre pontosabb és részletesebb
                          diagnosztikai felvételek készülnek a páciensekről. A gépi tanulás lehetőséget nyújt ezeknek a 
                          nagy mennyiségű diagnosztikai felvételeknek a gyorsan és hatékonyan történő feldolgozásában, a 
                          rákos és egyéb betegségek korai felismerésének és gyógyításának érdekében. """,
                          style={'text-align': 'justify', 'text-indent' : '10%', 'font-size' : '1.1em'}),
                     html.P("""A rákdiagnosztika fontossága és időszerűsége megkérdőjelezhetetlen, mivel Romániában és
                         Magyarországon is, a rákos megbetegedések okozta halálozások száma nagyon magas. Az IARC összesítése 
                         alapján Romániában 2018-ban 123.3 míg Magyarországon 155.8 volt a rákos megbetegedések halálozási
                         rátája 100 000 főhöz viszonyítva. """,style={'text-align': 'justify', 'text-indent' : '10%', 'font-size' : '1.1em'}),
                     html.P(
                         """A weboldal bemutatja a szakdolgozatohoz végzett kutatásokat, amelynek alapja a Kaggle
                          Histophathologic cancer detection nevű versenye""" ,style={'text-align': 'justify', 'text-indent' : '10%', 'font-size' : '1.1em'}),
                  ],md=5,
               ),
              dbc.Col(
                 [
                     html.Center(html.H2("Grafikon"),style={'font-family' : 'Times New Roman'}),
                     dcc.Graph(
                         figure={"data": [{"x": ['Magyaroszág','Szlovákia','Moldovai Köztársaság', 'Lengyelország', 'Románia', 'Bulgária', 'Ukrajna', 'Fehéroroszország', 'Csehország'],
                          "y": [155.8,141.4,137.1,136.5,123.3,119.4,118.7,109.7,106.5], 'type':'bar'}],
                          'layout':{'title':'Közép-Kelet-Európa rákos betegek halálozási rátája (/100 000 fő)', 'height' : '50%'}}
                     ),
                    
                ],),
            ]),
            dbc.Row(
                [
                    dbc.Col(
                    [
                        html.Br(),
                        html.Center(dbc.Button("A versenyről részletesen", color="secondary", href="https://www.kaggle.com/c/histopathologic-cancer-detection"))
                    ]),
                    dbc.Col([
                        html.Br(),
                        html.Center(dbc.Button("Hasonló grafikonok ebben a témában", color="secondary", href="https://gco.iarc.fr/today/home")) 
                    ])      
                ])
    ],className="mt-4",
)

def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SANDSTONE])
app.title = "Histopathology cancer detection"

app.layout = Homepage()

if __name__ == "__main__":
    app.run_server()