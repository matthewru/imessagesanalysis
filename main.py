from tkinter.tix import ExFileSelectBox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time, datetime
import seaborn as sns
sns.set_style('white')
from collections import Counter


df = pd.read_csv("imsgmeg.csv")
print(df.head())
print(df.iloc[:, 2])

theysent = 0
isent = 0
is_from_me = []
text = []
mytexts = []
theirtexts = []
for label, content in df.items():
    if label == "is_from_me":
        is_from_me = content.to_list()
    if label == "text":
        text = content.to_list()
for i in is_from_me:
    if i == 1:
        isent += 1
    else:
        theysent += 1
print(len(text))
print(len(is_from_me))
for i in range(len(text)):
    if (is_from_me[i] == 0):
        theirtexts.append(text[i])
    else:
        mytexts.append(text[i])
print(len(theirtexts))
mytextlength = 0
theirtextlength = 0
for i in mytexts:
    mytextlength += len(i)
for i in theirtexts:
    theirtextlength += len(i)
print("Meg:", theirtextlength)
print("Matthew:", mytextlength)
