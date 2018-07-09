import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import os
import plotly.graph_objs as go
from plotly import tools

app = dash.Dash()

css_directory = os.getcwd()
static_css_route = '/static/'
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


@app.server.route('{}<stylesheet>'.format(static_css_route))
def serve_stylesheet(stylesheet):
    return flask.send_from_directory(css_directory, stylesheet)


app.layout = html.Div([
       html.Link(
        rel='stylesheet',
        href='/static/stylesheet.css'
    ),
       html.Link(
        rel='stylesheet',
        href='/static/bootstrap.min.css'
    ),
    # Banner display
    html.Div([
        html.H2(
            'AES2.0 | Validation Report',
            id='title',
        style={'color':"#ffffff",'fontSize':'25px', 'fontWeight':'200', 'fontFamily': 'Arial',
                'textAlign':'center'}
        )
    ],
        className="banner",
        style={'background-color': "#272c33", 'color':"#ffffff", 
                'padding':'15px 0px 15px 25px'}
    ),

    html.Div(
        html.Div([
        html.Div(
             dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montral'},
                    ]}
                 ), className='col-12 col-md-6', style={'padding':'0px'}),
         html.Div(
            dcc.Graph(
                id='example-grap2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montral'},
                    ]}), className='col-12 col-md-6', style={'padding':'0px'}
            )], className='row'), className='container', style={'padding':'0px'}
    ),
        html.Hr(style={'margin':'0px 20px', 'border':'0', 'height':'1px', 'backgroundImage': 'linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0))'})]
    )

if __name__ == '__main__':
    app.run_server(debug=True)