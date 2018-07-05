import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import os

app = dash.Dash()

css_directory = os.getcwd()
stylesheets = ['stylesheet.css']
static_css_route = '/static/'
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
'''
@app.server.route('{}<stylesheet>'.format(static_css_route))
def serve_stylesheet(stylesheet):
    if stylesheet not in stylesheets:
        raise Exception(
            '"{}" is excluded from the allowed static files'.format(
                stylesheet
            )
        )
    return flask.send_from_directory(css_directory, stylesheet)

'''
@app.server.route('{}<stylesheet>'.format(static_css_route))
def serve_stylesheet(stylesheet):
    if stylesheet not in stylesheets:
        raise Exception(
            '"{}" is excluded from the allowed static files'.format(
                stylesheet
            )
        )
    return flask.send_from_directory(css_directory, stylesheet)


for stylesheet in stylesheets:
    app.css.append_css({"external_url": "/static/{}".format(stylesheet)})

app.layout = app.layout = html.Div([
       html.Link(
        rel='stylesheet',
        href='/static/stylesheet.css'
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

    html.Div(children=[


    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montral'},
            ],
            'layout': {
            }
        }
    )
])])

if __name__ == '__main__':
    app.run_server(debug=True)