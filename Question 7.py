#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 7: What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset? Please  just provide the number as answer.

import pandas as pd

# Read the filled CSV file
data = pd.read_csv('C:\Users\Zeynep\Downloads\country_vaccination_stats.csv')

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Filter data for 1/6/2021
vaccinations_on_2021_01_06 = data[data['date'] == '2021-01-06']

# Calculate total vaccinations on 1/6/2021
total_vaccinations_on_2021_01_06 = vaccinations_on_2021_01_06['daily_vaccinations'].sum()

print(total_vaccinations_on_2021_01_06)

