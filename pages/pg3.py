import dash
from dash import dcc, html
import plotly.express as px

#dash.register_page(__name__,
#                   path='/Employees in Industry',
#                   name='pg3',
#                   title='New heatmaps',
#                   image='pg3.png',
#                   description='Employees in Industry'
#)


dash.register_page(__name__, name='Employees in Industry')

layout = html.Div(
    [
        dcc.Markdown('## Employees Coming soon!', style={'textAlign':'center'})
#        dcc.Graph(figure= px.imshow([[1, 20, 30],
#                                     [20, 1, 60],
#                                     [30, 60, 1]]))
    ]
)