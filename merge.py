import glob
import json
print(glob.glob("Users/chaiwonpark/Desktop/excel/*.xlsx"))

import pandas as pd

# Read all three files into pandas dataframes
marketing_analyst_names = pd.read_excel("MarketingAnalystNames.xlsx")
sales_rep_names = pd.read_excel("SalesRepNames.xlsx")
senior_leadership_names = pd.read_excel("SeniorLeadershipNames.xlsx")

# Create a list of the files in order you want them appended
all_df_list = [marketing_analyst_names, sales_rep_names, senior_leadership_names]

# Merge all the dataframes in all_df_list
# Pandas will automatically append based on similar column names
appended_df = pd.concat(all_df_list)

# Write the appended dataframe to an excel file
# Add index=False parameter to not include row numbers
appended_df.to_excel("AllCompanyNames.xlsx", index=False)

import os

excelList = []
textFile = open("/Users/chaiwonpark/Desktop/excel/files.txt", "a+")
for root, dirs, files in os.walk("/Users/chaiwonpark/Desktop/excel"):
    for file in files:
        if file.endswith(".xlsx"):
            print(file)
            excelList.append(pd.read_excel(file))