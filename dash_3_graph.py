#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Date: 2020/03/30
# Author: Huiming
# Contact: kairu_madigan@yahoo.co.jp


import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2018, 2, 8)

df = web.DataReader("TSLA", "yahoo", start, end)
print(df.head())
