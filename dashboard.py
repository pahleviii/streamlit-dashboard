import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data():
    orders_df = pd.read_csv("olist_orders_dataset.csv")
    products_df = pd.read_csv("olist_products_dataset.csv")
    return orders_df, products_df

orders_df, products_df = load_data()

# Streamlit App
st.title("Dashboard Analisis Data Olist")

# Sidebar
st.sidebar.header("Opsi Filter")
status_filter = st.sidebar.multiselect("Pilih Status Pesanan", orders_df['order_status'].unique())

if status_filter:
    filtered_orders = orders_df[orders_df['order_status'].isin(status_filter)]
else:
    filtered_orders = orders_df

st.write("### Data Pesanan")
st.dataframe(filtered_orders.head())

# Visualisasi Status Pesanan
st.write("### Distribusi Status Pesanan")
fig, ax = plt.subplots()
order_counts = filtered_orders['order_status'].value_counts()
order_counts.plot(kind='bar', ax=ax)
ax.set_xlabel("Status")
ax.set_ylabel("Jumlah")
st.pyplot(fig)

# Visualisasi Berat Produk
st.write("### Distribusi Berat Produk")
fig, ax = plt.subplots()
sns.histplot(products_df['product_weight_g'].dropna(), bins=20, kde=True, ax=ax)
ax.set_xlabel("Berat Produk (g)")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

st.write("Dashboard ini menampilkan analisis dasar dari dataset Olist.")
