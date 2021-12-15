#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 13:21:09 2021

@author: yomarcummings
"""

import pandas as pd
import matplotlib.pyplot as plt
try:
    smpl_df = pd.read_csv("/data/highlights_data_sample.csv")
except FileNotFoundError:
    smpl_df = pd.read_csv("./data/highlights_data_sample.csv")


top_10 = smpl_df.head(10)

# top_10.set_index("occurred_at", inplace=True)
# Above line makes the "occurred_at" column as the index

xAxis = ["Yellow", "Green", "Pink", "Blue"]
yAxis = [6, 2, 1, 1]
# Results obtained from top_10["color"].value_counts()

plt.figure(figsize=(9, 3))
plt.bar(xAxis, yAxis, color=["yellow", "green", "pink", "blue"])
plt.title("Highlight Frequency vs Color")
plt.xlabel("Color")
plt.ylabel("Frequency")
# plt.grid(True)
plt.show()
