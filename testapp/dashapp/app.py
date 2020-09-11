import dash
import dash_html_components as html

import dpd_components as dpd

from django_plotly_dash import DjangoDash

app = DjangoDash('Example')  # replaces dash.Dash

app.layout = html.Div(
    [
        html.H1('Some text', id='text'),
        dpd.Pipe(id='live-update',
                 label="live_label",
                 channel_name="live_channel")
    ]
)


@app.callback(
    dash.dependencies.Output('text', 'children'),
    [dash.dependencies.Input('live-update', 'value')])
def live_update(value):
    return str(value)
