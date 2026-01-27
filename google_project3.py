import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
df = pd.read_csv("C:/Users/HP/Downloads/Play Store Data.csv")
 #Clean Installs
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Clean Category
df['Category'] = df['Category'].astype(str)

# Drop null installs
df = df.dropna(subset=['Installs'])
df['Size'] = df['Size'].str.replace('M','')
df = df[df['Size'].str.isnumeric()]
df['Size'] = df['Size'].astype(float)

df['Price'] = df['Price'].str.replace('$','', regex=False).astype(float)
df['Revenue'] = np.where(df['Type'] == 'Paid', df['Installs'] * df['Price'], 0)
df['Android_Ver_Num'] = df['Android Ver'].str.extract(r'(\d+\.\d+)').astype(float)
df['App_Name_Length'] = df['App'].str.len()
filtered_df = df[
    (df['Installs'] >= 10000) &
    (df['Revenue'] >= 10000) &
    (df['Android_Ver_Num'] > 4.0) &
    (df['Size'] > 15) &
    (df['Content Rating'] == 'Everyone') &
    (df['App_Name_Length'] <= 30)
]
top_categories = (
    filtered_df.groupby('Category')['Installs']
    .sum()
    .sort_values(ascending=False)
    .head(3)
    .index
)

filtered_df = filtered_df[filtered_df['Category'].isin(top_categories)]
summary = (
    filtered_df
    .groupby(['Type','Category'])
    .agg(
        Avg_Installs=('Installs','mean'),
        Avg_Revenue=('Revenue','mean')
    )
    .reset_index()
)
ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
current_hour = ist_time.hour
if not (13 <= current_hour < 14):
    print("⏰ This visualization is available only between 1 PM and 2 PM IST.")
if 13 <= current_hour < 14:

    fig = go.Figure()

    # Bar: Average Installs
    fig.add_trace(
        go.Bar(
            x=summary['Type'],
            y=summary['Avg_Installs'],
            name='Average Installs'
        )
    )

    # Line: Average Revenue (Secondary Axis)
    fig.add_trace(
        go.Scatter(
            x=summary['Type'],
            y=summary['Avg_Revenue'],
            name='Average Revenue',
            yaxis='y2',
            mode='lines+markers'
        )
    )

    fig.update_layout(
        title="Free vs Paid Apps: Average Installs vs Revenue",
        xaxis_title="App Type",
        yaxis=dict(title="Average Installs"),
        yaxis2=dict(
            title="Average Revenue ($)",
            overlaying='y',
            side='right'
        ),
        legend_title="Metrics",
        template="plotly_white"
    )

    fig.show()





