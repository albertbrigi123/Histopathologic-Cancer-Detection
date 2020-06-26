import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from keras.models import load_model
from aboutdata import AboutData
from classifiers import Classifiers
from homepage import Homepage
from classification import Classification
from keras.preprocessing import image
import numpy as np
import base64
import os



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])

app.config.suppress_callback_exceptions = True
app.title = "Histopathology cancer detection"
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/aboutdata':
        return AboutData()
    if pathname == '/classifiers':
        return Classifiers()
    if pathname == '/classification':
        return Classification()
    else:
        return Homepage()

def get_model(path): 
    model = load_model(path)
    print("model loaded")
    return model

global  model1, model2
model1 = get_model("../models/model0.h5")
model2 = get_model("../models/model1.h5")

def model_predict( model):
    img = image.load_img('./asd.png', target_size=(96,96)) 
    x = image.img_to_array(img)
    x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    return preds



def parse_contents(contents, filename, date):
  
    save_picture(contents)
    pred1 = model_predict(model1)
    pred2 = model_predict(model2)
   

    return html.Div([
        html.Img(src=contents, style={
            'display': 'block',
            'margin-left': 'auto',
            'margin-right': 'auto',
            'width': '22%',
        }),
        html.Br(),
        html.Br(),
        html.Center(html.P('Pabló Gómez és csapata osztályozójának jósolt értéke: {}'.format(
       pred1[0][0]),style={'font-family' : 'Times New Roman', 'font-size' : '1.5em'})),
       html.Br(),
       html.Center(html.P('Marsh modellje által jósolt érték {}'.format(
       pred2[0][1]),style={'font-family' : 'Times New Roman', 'font-size' : '1.5em'})),
       
       html.Center(html.P("Jelmagyarázat: 0 - egészséges,  1 - beteg", style={'font-family' : 'Times New Roman', 'font-size' : '1.2em'}))
    
        
    ])



def save_picture(contents):
    data = contents.encode("utf8").split(b";base64,")[1]
    with open(os.path.join("./", "asd.png"), "wb") as fp:
        fp.write(base64.decodebytes(data))

@app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents')],
              [State('upload-image', 'filename'),
               State('upload-image', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

    
  

    
    

if __name__ == '__main__':
    app.run_server(debug=True)
