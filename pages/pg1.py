import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

# To create meta tag for each page, define the title, image, and description.

#dash.register_page(__name__,
#                   path='/Building Portfolio',  # '/' is home page and it represents the url
#                   name='pg1',  # name of page, commonly used as name of link
#                   title='Index',  # title that appears on browser's tab
#                   image='pg1.png',  # image in the assets folder
#                   description='Histograms are the new bar charts'
#)

dash.register_page(__name__, name='Real Estate Portfolio')

# page 1 data
df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Markdown('## Real Estate Portfolio Coming soon!', style={'textAlign':'center'})
#        dbc.Row(
#            [
#                dbc.Col(
#                    [
#                        dcc.Dropdown(options=df.continent.unique(),
#                                     id='cont-choice')
#                    ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
#                )
#            ]
#        ),
#        dbc.Row(
#            [
#                dbc.Col(
#                    [
#                        dcc.Graph(id='line-fig',
#                                  figure=px.histogram(df, x='continent',
#                                                      y='lifeExp',
#                                                      histfunc='avg'))
#                    ], width=12
#                )
#            ]
#        )
    ]
)


@callback(
    Output('line-fig', 'figure'),
    Input('cont-choice', 'value')
)
def update_graph(value):
    if value is None:
        fig = px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
    else:
        dff = df[df.continent==value]
        fig = px.histogram(dff, x='country', y='lifeExp', histfunc='avg')
    return fig