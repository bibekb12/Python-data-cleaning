import pandas as pd

#loading the dataset from the file
df = pd.read_csv("D:\\working-AI\\dataset-raw\\rhs_2005.csv")

#checking the data
# print(df.head)

#checking for the missing data
# print(df.isna().sum())

#replace the string 'NA' with actual NaN
df.replace('NA', pd.NA, inplace=True)

#convert all numeric columns property (except 'State/UT')
cols_to_convert = df.columns.drop('State/UT')
df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric,errors='coerce')

#option: Fill missing values with 0 (or use mean() median() etc)
df.fillna(0, inplace=True)

#rename columns for the clearity
df.columns.str.strip().str.replace('','_').str.replace('/','_')

# print(df.info())
# print(df.describe())
# print(df.head())