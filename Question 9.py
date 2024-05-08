#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re

# Sample data
data = {
    'Device_Type': ['AXO145', 'TRU151', 'Z0D231', 'YRT226', 'LWR245'],
    'Stats_Access_Link': [
        '<url>https://xcd32112.smart_meter.com</url>',
        '<url>http://tXh67.dia_meter.com</url>',
        '<url=http://yT5495.smart_meter.com</url>',
        '<url>https://ret323_TRu.crown.com</url>',
        '<url=nttos://luwr3243.celcius.come</url>'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to extract pure URL
def extract_url(link):
    # Regular expression to extract URL
    pattern = r'<url(?:=.+)?>(https?://[\w\d._-]+)</url>'
    match = re.search(pattern, link, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None

# Apply function to each row
df['Pure_URL'] = df['Stats_Access_Link'].apply(extract_url)

# Display DataFrame
print(df)

