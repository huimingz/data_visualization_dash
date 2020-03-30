#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Date: 2020/03/30
# Author: Huiming
# Contact: kairu_madigan@yahoo.co.jp

import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from dash.dependencies import Input, Output

start = datetime.datetime(2018, 1, 1)
# end = datetime.datetime.now()

stock = "TSLA"
# df = web.DataReader(name=stock, data_source="yahoo", start=start, end=end)

app = dash.Dash()

app.layout = html.Div(children=[
    # html.H1(children="Hello Dash"),
    html.Div(children="Symbol To Graph:"),
    dcc.Input(id="input", value="yahoo", type="text"),
    html.Div(id="output-graph")
    # dcc.Graph(
    #     id="example-graph",
    #     figure={
    #         "data": [
    #             {"x": df.index, "y": df.Close, "type": "line", "name": "SF"},
    #         ],
    #         "layout": {
    #             "title": stock
    #         }
    #     }
    # )
])


@app.callback(
    output=Output(component_id="output-graph", component_property="children"),
    inputs=[Input(component_id="input", component_property="value")]
)
def update_graph(input_data):
    end = datetime.datetime.now()
    df = web.DataReader(name=input_data, data_source="yahoo", start=start, end=end)
    graph = dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": df.index, "y": df.Close, "type": "line", "name": input_data}
            ],
            "layout": {
                "title": input_data,
            }
        }
    )
    return graph


if __name__ == "__main__":
    app.run_server(debug=True)
