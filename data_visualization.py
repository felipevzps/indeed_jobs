import os
import pandas as pd
import matplotlib.pyplot as plt

relative_data_path = "./data/bioinfo12012020_05:15.csv"
fname = os.path.basename(relative_data_path)

df1 = pd.read_csv(relative_data_path, encoding="utf-8")

df = df1.drop_duplicates()
print(df.shape)

#Task 1: Find companies with highest number of job listings
fig1 = plt.gcf()
counts = df.groupby("Company").count()["Title"].sort_values(ascending=False)#[:20]
plt.show(counts.plot(kind="bar", figsize=(30,15)))
fig1.tight_layout()
fig1.savefig("./plot/company_"+fname+".pdf")

#Task 2: Find Locations with highest number of job listings
fig2 = plt.gcf()
loc_counts = df.groupby("Location").count()["Title"].sort_values(ascending=False)[:30]
plt.show(loc_counts.plot(kind="bar", figsize=(30,15)))
fig2.tight_layout()
fig2.savefig("./plot/location_"+fname+".pdf")



