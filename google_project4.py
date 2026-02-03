import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz
df = pd.read_csv("C:/Users/HP/Downloads/Play Store Data.csv")
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df['Month'] = df['Last Updated'].dt.to_period('M').astype(str)
df['Installs'] = (
    df['Installs']
    .str.replace('[+,]', '', regex=True)
)

df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
filtered_df = df[
    (df['Reviews'] > 500) &
    (~df['App'].str.startswith(('x', 'y', 'z'), na=False)) &
    (~df['App'].str.contains('S', na=False)) &

    (df['Category'].str.startswith(('E','C','B')))
]
category_map = {
    'Beauty': 'सौंदर्य',          # Hindi
    'Business': 'வணிகம்',         # Tamil
    'Dating': 'Partnersuche'      # German
}

df['Category_Localized'] = df['Category'].map(category_map).fillna(df['Category'])
trend = (
    df.groupby(['Month','Category_Localized'])['Installs']
      .sum()
      .reset_index()
      .sort_values('Month')
)
trend['MoM_Growth'] = (
    trend.groupby('Category_Localized')['Installs']
         .pct_change()
)

trend['High_Growth'] = trend['MoM_Growth'] > 0.20
ist = pytz.timezone('Asia/Kolkata')
current_hour = datetime.now(ist).hour
if 18 <= current_hour < 21:

    fig = px.line(
        trend,
        x='Month',
        y='Installs',
        color='Category_Localized',
        markers=True,
        title='Task 4 – Monthly Install Growth by Category'
    )

    fig.update_traces(
        marker=dict(size=6),
        line=dict(width=2)
    )

    fig.show()

else:
    print("This visualization is available only between 6 PM and 9 PM IST.")
