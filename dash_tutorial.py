#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Date: 2020/03/30
# Author: Huiming
# Contact: kairu_madigan@yahoo.co.jp

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

# 简单使用
# app.layout = html.Div(children=[
#     html.H1("Dash tutorialsss"),
#     dcc.Graph(id="example", figure={
#         "data": [
#             {"x": [1, 2, 3, 4, 5], "y": [5, 6, 7, 2, 4], "type": "line", "name": "boats"},
#             {"x": [1, 2, 3, 4, 5], "y": [1, 2, 7, 6, 3], "type": "bar", "name": "cars"},
#         ],
#         "layout": {
#             "title": "Basic Dash Example",
#         }
#     })
# ])

# 输入内容实时返回
app.layout = html.Div(children=[
    dcc.Input(id="input", value="Enter something", type="text"),
    html.Div(id="output", )
])


@app.callback(
    output=Output(component_id="output", component_property="children"),
    inputs=[Input(component_id="input", component_property="value")]
)
def update_value(input_data):
    try:
        return f"{float(input_data) ** 2}"
    except ValueError as err:
        return f"Some error occurred: {err}"


if __name__ == "__main__":
    app.run_server(debug=True)
