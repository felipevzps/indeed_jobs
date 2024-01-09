#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import os
import obo
import argparse

parser = argparse.ArgumentParser(description="A script to generate histograms from Indeed job listings.")
parser.add_argument("--i", dest = 'input', type=str, metavar="data/OUTPUT_NAME", required=True, help="Output name <saved on data/>")

args = parser.parse_args()
relative_data_path = args.input

#Input data
fname = os.path.basename(relative_data_path)

df1 = pd.read_csv(relative_data_path, encoding="utf-8")
df = df1.drop_duplicates()

companies = obo.getJobsByCompanies(df) 
companies.plot(kind="bar", figsize=(30,15))
plt.savefig("./plot/JobsByCompanies_"+fname+".png")
#plt.show()

locations = obo.getJobLocation(df)
locations.plot(kind="bar", figsize=(30,15))
plt.savefig("./plot/JobLocation_"+fname+".png")
#plt.show()

wordlist = obo.getJobKeywords(df)
wordlist = obo.removeStopWords(wordlist, obo.stopwords)

extracted_df = obo.calculateKeywordFrequency(wordlist,4)
extracted_df.plot(x ='wordlist', y='wordfreq', kind='bar', figsize=(30,15))
plt.savefig("./plot/KeywordFrequencie_"+fname+".png")
#plt.show()
