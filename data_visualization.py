import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

df1 = pd.read_csv("./bioinfo.csv", encoding="utf-8")

df = df1.drop_duplicates()
print(df.shape)

#Task 1: Find companies with highest number of job listings
counts = df.groupby("Empresa").count()["Titulo"].sort_values(ascending=False)#[:20]
#plt.show(counts.plot(kind="bar", figsize=(30,15)))

#Task 2: Find Locations with highest number of job listings
loc_counts = df.groupby("Local").count()["Titulo"].sort_values(ascending=False)[:30]
#plt.show(loc_counts.plot(kind="bar", figsize=(30,15)))


