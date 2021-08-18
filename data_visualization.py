import matplotlib.pyplot as plt
import pandas as pd
import os
import obo

#Input data
relative_data_path = "data/EstagioDesigner_SP.csv"
fname = os.path.basename(relative_data_path)

df1 = pd.read_csv(relative_data_path, encoding="utf-8")
df = df1.drop_duplicates()

#fig1 = plt.gcf()
companies = obo.getJobsByCompanies(df) 
#plt.savefig("./plot/JobsByCompanies_"+fname+".pdf")
plt.show(companies.plot(kind="bar", figsize=(30,15)))

#fig2 = plt.gcf()
locations = obo.getJobLocation(df)
#plt.savefig("./plot/JobLocation_"+fname+".pdf")
plt.show(locations.plot(kind="bar", figsize=(30,15)))

wordlist = obo.getJobKeywords(df)
wordlist = obo.removeStopWords(wordlist, obo.stopwords)

#fig3 = plt.gcf()
extracted_df = obo.calculateKeywordFrequency(wordlist,4)
#plt.savefig("./plot/KeywordFrequencie_"+fname+".pdf")
plt.show(extracted_df.plot(x ='wordlist', y='wordfreq', kind='bar', figsize=(30,15)))
