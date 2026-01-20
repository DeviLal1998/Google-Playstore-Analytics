# data cleaning
import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/Play Store Data.csv")


df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).str.replace('Free', '0', regex=False).astype(int)
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

df['Size'] = df['Size'].str.replace('M','')
df = df[df['Size'].str.isnumeric()]
df['Size'] = df['Size'].astype(float)

df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df['Update_Month'] = df['Last Updated'].dt.month_name()
# filter conditions
filtered_df = df[
    (df['Rating'] >= 4.0) &
    (df['Size'] >= 10) &
    (df['Update_Month'] == 'January')
]
#top 10 categories by installs
top_categories = (
    filtered_df
    .groupby('Category')
    .agg({
        'Installs': 'sum',
        'Rating': 'mean',
        'Reviews': 'sum'
    })
    .sort_values('Installs', ascending=False)
    .head(10)
)
#grouped bar chart
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(top_categories.index))
width = 0.35

plt.figure()
plt.bar(x - width/2, top_categories['Rating'], width, label='Avg Rating')
plt.bar(x + width/2, top_categories['Reviews']/1e6, width, label='Total Reviews (Millions)')

plt.xticks(x, top_categories.index, rotation=45)
plt.ylabel("Values")
plt.title("Top 10 Categories: Rating vs Reviews")
plt.legend()
plt.show()


from datetime import datetime
import pytz
import streamlit as st

ist = pytz.timezone('Asia/Kolkata')
hour = datetime.now(ist).hour

if 15 <= hour < 17:
    st.pyplot(plt)
else:
    st.warning("This chart is available only between 3 PM – 5 PM IST")



