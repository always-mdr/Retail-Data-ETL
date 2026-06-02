import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Retail Data Dashboard", layout="wide")
st.title("🛒 Retail Sales Dashboard")
st.markdown("Visualizing cleaned data from the local SQLite database.")

@st.cache_data
def load_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    db_path = os.path.join(project_root, 'data', 'sales.db')
    
    if not os.path.exists(db_path):
        return pd.DataFrame()
        
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM orders", conn)
    conn.close()
    
    if not df.empty:
        df['order_date'] = pd.to_datetime(df['order_date'])
        
    return df

df = load_data()

if df.empty:
    st.warning("No data found! Please run the ETL pipeline first: `make run`")
else:
    # Top Level Metrics
    total_revenue = df['total_amount'].sum()
    total_orders = df['order_id'].nunique()
    total_items = df['quantity'].sum()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Total Unique Orders", f"{total_orders:,}")
    col3.metric("Total Items Sold", f"{total_items:,}")
    
    st.divider()
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Revenue by Product")
        product_revenue = df.groupby('product')['total_amount'].sum().reset_index()
        fig_prod = px.pie(product_revenue, values='total_amount', names='product', hole=0.4)
        st.plotly_chart(fig_prod, use_container_width=True)
        
    with col_right:
        st.subheader("Daily Sales Trend")
        daily_sales = df.groupby('order_date')['total_amount'].sum().reset_index()
        fig_trend = px.line(daily_sales, x='order_date', y='total_amount', markers=True)
        st.plotly_chart(fig_trend, use_container_width=True)
        
    st.subheader("Clean Data Preview")
    st.dataframe(df.head(100))
