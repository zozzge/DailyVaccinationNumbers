#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 6: Code Implementation Task: Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.
#Please  provide the link to your code as answer to this question.

import pandas as pd

# Read the filled CSV file
data = pd.read_csv('C:\Users\Zeynep\Downloads\country_vaccination_stats.csv')

# Calculate median daily vaccination numbers for each country
median_daily_vaccinations = data.groupby('country')['daily_vaccinations'].median()

# Sort countries by median daily vaccination numbers and get top 3
top_3_countries = median_daily_vaccinations.sort_values(ascending=False).head(3)

print("Top-3 countries with highest median daily vaccination numbers:")
print(top_3_countries)

