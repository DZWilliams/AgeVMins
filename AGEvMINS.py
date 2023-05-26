# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:03:51 2023

@author: DZWilliams
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from datetime import date

#read in the CSV file
df = pd.read_csv("agevmins.csv")
dfFCSP = (df.loc[(df["Squad"]=="Hamburger SV")])
#dfFCSP = (df.loc[(df["Squad"]=="St. Pauli")])

print(df.info())

fig, ax = plt.subplots()
plt.scatter(x="Age", y="Min", data=df, color="lightgrey")
plt.scatter(x="Age", y="Min", data=dfFCSP, color="blue")
plt.xlim(14,40)
plt.ylim(0,3200)
plt.xlabel("Age")
plt.ylabel("Mins")
plt.title("Age of the St Pauli Squad and Mins Played")
plt.show()