#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import all possibly helpful packages
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[ ]:


# Access the csv files of extracted metabolite ms data set of 
# symptoms from github repo
df_severe_metabolite_ms = pd.read_csv ("~/Documents/GitHub/440_project/Data/Processed_Severe_Metabolite_MS_Data.csv")
df_mild_metabolite_ms = pd.read_csv ("~/Documents/GitHub/440_project/Data/Processed_Mild_Metabolite_MS_Data.csv")
df_asymptomatic_metabolite_ms = pd.read_csv ("~/Documents/GitHub/440_project/Data/Processed_Asymptomatic_Metabolite_MS_Data.csv")


# In[ ]:


display (df_severe_metabolite_ms)
display (df_mild_metabolite_ms)
display (df_asymptomatic_metabolite_ms)


# In[ ]:


# Function input: df of the extracted metabolite ms data set of 
# corresponding symptoms. Output: number of raw MS reads for '4-Aminophenol'
# and the corresponding patient sample ID
def get_4_aminophenol (df_input):
    for a in range (len(df_input)):
        if df_input.iloc[a,1] == '4-Aminophenol':
            aminophenol = df_input.iloc[a,2:]
            for b in range (len(aminophenol)):
                aminophenol[b] = int(aminophenol[b])
            aminophenol = np.array(aminophenol)
    patientid = df_input.iloc[1,2:]
#for c in range (len(df_input.columns)):
#patientid[c] = int(patientid[c])
    patientid = np.array(patientid)
    return [aminophenol,patientid]


# In[ ]:


# Get those information for the three symptoms
[aminophenol_severe, severe_patient_id]= get_4_aminophenol(df_severe_metabolite_ms)
[aminophenol_mild, mild_patient_id] = get_4_aminophenol(df_mild_metabolite_ms)
[aminophenol_asymptomatic, asymptomatic_patient_id] = get_4_aminophenol(df_asymptomatic_metabolite_ms)


# In[ ]:


# Plot on different plots due to different x axis
# (different number of patient samples in each group)
fig1, ax1i = plt.subplots()
fig2, ax2i = plt.subplots()
fig3, ax3i = plt.subplots()

ax1i.bar(severe_patient_id, aminophenol_severe, label='Severe Covid')
ax2i.bar(mild_patient_id, aminophenol_mild, label='Mild Covid')
ax3i.bar(asymptomatic_patient_id, aminophenol_asymptomatic, label='Asymptomatic Covid')

ax1i.set_xlabel('Sample ID')
ax1i.title.set_text('4-Aminophenol Level')
ax2i.set_xlabel('Sample ID')
ax2i.title.set_text('4-Aminophenol Level')
ax3i.set_xlabel('Sample ID')
ax3i.title.set_text('4-Aminophenol Level')

ax1i.set(ylim=(0, 150000))
ax2i.set(ylim=(0, 150000))
ax3i.set(ylim=(0, 150000))

ax1i.set_xticks(range(len(severe_patient_id)))
ax1i.set_xticklabels(severe_patient_id, rotation=90, ha='right', fontsize=3)
ax1i.tick_params(axis='x', which='major', labelsize=3)
ax2i.set_xticks(range(len(mild_patient_id)))
ax2i.set_xticklabels(mild_patient_id, rotation=90, ha='right', fontsize=3)
ax2i.tick_params(axis='x', which='major', labelsize=3)
ax3i.set_xticks(range(len(asymptomatic_patient_id)))
ax3i.set_xticklabels(asymptomatic_patient_id, rotation=90, ha='right', fontsize=3)
ax3i.tick_params(axis='x', which='major', labelsize=3)

ax1i.legend()
ax2i.legend()
ax3i.legend()
plt.show()


# In[ ]:


fig1.savefig('./Raw_4-Aminophenol_Level_Severe_Covid.pdf', bbox_inches='tight')
fig2.savefig('./Raw_4-Aminophenol_Level_Mild_Covid.pdf', bbox_inches='tight')
fig3.savefig('./Raw_4-Aminophenol_Level_Asymptomatic_Covid.pdf', bbox_inches='tight')


# In[1]:


pipreqs 


# In[ ]:




