import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/sales_data.csv')
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    return df

df = load_data()

st.title("📊 Sales Performance Dashboard")

# Filters
year = st.sidebar.multiselect(
    "Year", sorted(df['Year'].unique()), default=sorted(df['Year'].unique())
)
region = st.sidebar.selectbox("Region", ['All'] + sorted(df['Region'].unique()))

filtered = df[df['Year'].isin(year)]
if region != 'All':
    filtered = filtered[filtered['Region'] == region]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Revenue", f"₹{filtered['Revenue'].sum():,.0f}")
col2.metric("Profit", f"₹{filtered['Profit'].sum():,.0f}")
col3.metric("Orders", len(filtered))

# Charts
st.subheader("Revenue by Region")
region_chart = filtered.groupby('Region')['Revenue'].sum().reset_index()
fig1 = px.bar(region_chart, x='Region', y='Revenue')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Top Cities by Profit")
city_chart = filtered.groupby('City')['Profit'].sum().reset_index()
city_chart = city_chart.sort_values('Profit', ascending=False).head(10)
fig2 = px.bar(city_chart, x='Profit', y='City', orientation='h')
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Monthly Trend")
monthly = filtered.groupby(filtered['Order_Date'].dt.to_period('M'))[['Revenue','Profit']].sum().reset_index()
monthly['Order_Date'] = monthly['Order_Date'].astype(str)
fig3 = px.line(monthly, x='Order_Date', y=['Revenue','Profit'])
st.plotly_chart(fig3, use_container_width=True)

st.success("✅ Dashboard running successfully")
