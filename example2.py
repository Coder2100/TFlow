 #-*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

    """
    Areas to customize
we modified the inline styles of the html.Div and html.H1 components with the style property.
The keys in the style dictionary are camelCased. So, instead of text-align, it's textAlign.
The style property in HTML is a semicolon-separated string. In Dash, you can just supply a dictionary
html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'}) is rendered in the Dash application as <h1 style="text-align: center; color: #7FDBFF">Hello Dash</h1>.
The children of the HTML tag is specified through the children keyword argument. By convention, this is always the first argument and so it is often omitted.

    """