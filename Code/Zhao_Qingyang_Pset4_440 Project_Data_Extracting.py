#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import all possibly important packages
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[ ]:


# Read the raw data csv file on mac desktop
df_rawdata = pd.read_csv ("~/Desktop/ST002301_AN003757 copy.csv")
print (df_rawdata)


# In[ ]:


# Two for loops to show where the two meaningful data sets start and end
for i in range (len(df_rawdata)):
    if df_rawdata.iloc[i,0] == 'MS_METABOLITE_DATA_START':
        row_start = i
    if df_rawdata.iloc[i,0] == 'MS_METABOLITE_DATA_END':
        row_end = i
    if df_rawdata.iloc[i,0] == 'METABOLITES_START':
        sec_row_start = i
    if df_rawdata.iloc[i,0] == 'METABOLITES_END':
        sec_row_end = i
print (row_start, row_end)
print (sec_row_start, sec_row_end)


# In[ ]:


# Identify the section of rows to extract for the first meaningful data piece
# which is the MS reading of metabolites
# store in an empty same dimension dataframe
row_num = row_end-row_start
column_num = len(df_rawdata.columns)
df_metabolites_ms = pd.DataFrame(index=range(row_num),columns=range(column_num))
count = 0
for a in range (row_start, row_end):
    df_metabolites_ms.iloc[count] = df_rawdata.iloc[a]
    count = count + 1
display(df_metabolites_ms)


# In[ ]:


# Save the extracted file
df_metabolites_ms.to_csv('Processed_Metabolite_MS_Data.csv') 


# In[ ]:


# Same procedure to extract the metabolite read information 
# the second piece of important data
sec_row_num = sec_row_end - sec_row_start
column_num = len(df_rawdata.columns)
df_metabolite = pd.DataFrame(index=range(sec_row_num),columns=range(column_num))
count = 0
for b in range (sec_row_start, sec_row_end):
    df_metabolite.iloc[count] = df_rawdata.iloc[b]
    count = count + 1
display(df_metabolite)


# In[ ]:


# Get rid of any redundant columns (previous rows/data sections have info
# in those columns but not here)
df_metabolite = df_metabolite.drop(df_metabolite.columns[9:], axis=1)
display (df_metabolite)


# In[ ]:


df_metabolite.to_csv('Processed_Metabolites_Data.csv') 


# In[ ]:


# For loops going through the columns on the row with symptom info
# to identify which group the sample (each column)
# belongs to, and store them
severe_col = [0]
mild_col = [0]
asymptomatic_col = [0]
for c in range (len(df_metabolites_ms.columns)):
    if df_metabolites_ms.iloc[2,c] == 'Severity of Disease:Severe':
        severe_col = np.append(severe_col,c)
    if df_metabolites_ms.iloc[2,c] == 'Severity of Disease:Mild':
        mild_col = np.append(mild_col,c)
    if df_metabolites_ms.iloc[2,c] == 'Severity of Disease:Asymptomatic':
        asymptomatic_col = np.append(asymptomatic_col,c)

print(severe_col)
print(mild_col)
print(asymptomatic_col)


# In[ ]:


# Create empty df with dimensions same to the corresponding patient symptom group df
df_severe = pd.DataFrame(index=range(row_num),columns=range(len(severe_col)))
df_mild = pd.DataFrame(index=range(row_num),columns=range(len(mild_col)))
df_asymptomatic = pd.DataFrame(index=range(row_num),columns=range(len(asymptomatic_col)))

# Function with inputs of original extracted "processed metabolites ms df",
# empty df for that patient group, and the stored column numbers
# output to generate new dataframe corresponding to different symptoms
def sortbyseverity (df_ori, df_mod, col_nums):
    count = 0
    for e in range (len(col_nums)):
        col_pos = int(col_nums[e])
        df_mod.iloc[:,count] = df_ori.iloc[:,col_pos]
        count = count+1
    return df_mod

df_severe_metabolite_ms = sortbyseverity(df_metabolites_ms,df_severe,severe_col)
df_mild_metabolite_ms = sortbyseverity(df_metabolites_ms,df_mild,mild_col)
df_asymptomatic_metabolite_ms = sortbyseverity(df_metabolites_ms,df_asymptomatic,asymptomatic_col)


# In[ ]:


df_severe_metabolite_ms.to_csv('Processed_Severe_Metabolite_MS_Data.csv')
df_mild_metabolite_ms.to_csv('Processed_Mild_Metabolite_MS_Data.csv')
df_asymptomatic_metabolite_ms.to_csv('Processed_Asymptomatic_Metabolite_MS_Data.csv')

