#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Date: 2020/03/30
# Author: Huiming
# Contact: kairu_madigan@yahoo.co.jp

import dash
from dash.dependencies import Output, Event

import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

x = deque(maxlen=20)
y = deque(maxlen=20)
x.append(1)
y.append(1)

app = dash.Dash(name=__name__)
app.layout = html.Div([
    dcc.Graph(id="live-graph", animate=True),
    dcc.Interval(id="graph-update", interval=100)
])


@app.callback(
    output=Output(component_id="live-graph", component_property="figure"),
    events=[Event(component_id="graph-update", component_event="interval")]
)
def update_graph():
    global x
    global y

    x.append(x[-1] + 1)
    y.append(y[-1] + y[-1] *random.uniform(-0.1, 0.1))

    data = go.Scatter(
        x=list(x),
        y=list(y),
        name="Scatter",
        mode="lines+markers",
    )
    return {
        "data": [data],
        "layout": go.Layout(
            xaxis=dict(range=[min(x), max(x)]),
            yaxis=dict(range=[min(y), max(y)])
        )
    }


if __name__ == "__main__":
    app.run_server(debug=True)
