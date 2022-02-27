import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Kantar - APP",
    layout='wide'
)


@st.cache(ttl=24 * 60 * 60)
def read_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
    data = pd.read_excel(url)
    data['total_price'] = data['UnitPrice'] * data['Quantity']
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data = data[data['total_price'] >= 0]
    return data


data = read_data()
col1, col2 = st.columns(2)

country = st.sidebar.selectbox('Select a column',
                               options=data['Country'].unique().tolist())
filtered_data = data[(data['Country'] == country) &
                     (~data['CustomerID'].isnull())]
with col1:
    sales = filtered_data.resample(on='InvoiceDate', rule='1d')['total_price'].sum()
    fig = plt.figure()
    plt.plot(sales.index, sales.values)
    plt.title('Daywise Sales')
    st.pyplot(fig)
with col2:
    sales = filtered_data.resample(on='InvoiceDate', rule='1m')['total_price'].sum()
    fig = plt.figure()
    plt.plot(sales.index, sales.values)
    plt.title('Monthwise Sales')
    st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    filtered_data['CustomerID'] = filtered_data['CustomerID'].apply(lambda v: 'Customer ' + str(v))
    sales = filtered_data.groupby(['CustomerID'])['total_price'].sum().sort_values(ascending=False).head(10)
    fig = plt.figure()
    plt.bar(sales.index, sales.values)
    plt.title('Top 10 customers')
    plt.xticks(rotation=45)
    st.pyplot(fig)
with col2:
    filtered_data['StockCode'] = filtered_data['StockCode'].apply(lambda v: 'Product ' + str(v))
    sales = filtered_data.groupby(['StockCode'])['total_price'].sum().sort_values(ascending=False).head(10)
    fig = plt.figure()
    plt.bar(sales.index, sales.values)
    plt.title('Top 10 Products')
    plt.xticks(rotation=45)
    st.pyplot(fig)

