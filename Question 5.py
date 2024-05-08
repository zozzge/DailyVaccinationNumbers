#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 5: Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.  
#Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero). 
#Please  provide the link to your code as answer to this question.

import pandas as pd

# Read the CSV file
data = pd.read_csv('C:\Users\Zeynep\Downloads\country_vaccination_stats.csv')

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Sort data by country and date
data = data.sort_values(by=['country', 'date'])

# Fill missing values with 0
data['daily_vaccinations'] = data['daily_vaccinations'].fillna(0)

# Group by country and fill missing values with minimum daily vaccination number
data['daily_vaccinations'] = data.groupby('country')['daily_vaccinations'].transform(lambda x: x.fillna(x.min()))

# Convert daily_vaccinations column to integer
data['daily_vaccinations'] = data['daily_vaccinations'].astype(int)

# Save the filled data to a new CSV file
data.to_csv("filled_vaccination_data.csv", index=False)

