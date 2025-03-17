import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
def load_data():
    orders_df = pd.read_csv("olist_orders_dataset.csv")
    products_df = pd.read_csv("olist_products_dataset.csv")
    return orders_df, products_df

orders_df, products_df = load_data()

# Streamlit App
st.title("📊 Dashboard Analisis Data Olist")

# Sidebar
st.sidebar.header("Opsi Filter")
status_filter = st.sidebar.multiselect("Pilih Status Pesanan", orders_df['order_status'].unique())

if status_filter:
    filtered_orders = orders_df[orders_df['order_status'].isin(status_filter)]
else:
    filtered_orders = orders_df

st.write("### 🛒 Data Pesanan")
st.dataframe(filtered_orders.head())

# Visualisasi Status Pesanan
st.write("### 📈 Distribusi Status Pesanan")
fig, ax = plt.subplots()
order_counts = filtered_orders['order_status'].value_counts()
order_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_xlabel("Status")
ax.set_ylabel("Jumlah")
st.pyplot(fig)

# Visualisasi Berat Produk
st.write("### ⚖️ Distribusi Berat Produk")
fig, ax = plt.subplots()
sns.histplot(products_df['product_weight_g'].dropna(), bins=20, kde=True, ax=ax, color='orange')
ax.set_xlabel("Berat Produk (g)")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

# Rata-rata Panjang Deskripsi Produk Berdasarkan Jumlah Foto
st.write("### 📝 Rata-rata Panjang Deskripsi Produk")
kategori = st.selectbox("Pilih Kategori Produk:", products_df["product_category_name"].dropna().unique())
data_kategori = products_df[products_df["product_category_name"] == kategori]
avg_description_length = data_kategori.groupby("product_photos_qty")["product_description_lenght"].mean()

fig, ax = plt.subplots()
avg_description_length.plot(kind="bar", color="green", ax=ax)
ax.set_title(f"Panjang Deskripsi vs. Jumlah Foto ({kategori})")
ax.set_xlabel("Jumlah Foto Produk")
ax.set_ylabel("Rata-rata Panjang Deskripsi")
st.pyplot(fig)

# Kategori dengan Berat Produk Tertinggi
st.write("### 🔝 Kategori dengan Berat Produk Tertinggi")
avg_weight_per_category = products_df.groupby("product_category_name")["product_weight_g"].mean()
highest_weight_category = avg_weight_per_category.idxmax()
highest_weight_value = avg_weight_per_category.max()
st.write(f"Kategori dengan rata-rata berat tertinggi: **{highest_weight_category} ({highest_weight_value} gram)**")

fig, ax = plt.subplots()
products_df[products_df["product_category_name"] == highest_weight_category]["product_weight_g"].plot(kind="hist", bins=20, color="red", alpha=0.7, ax=ax)
ax.set_title(f"Distribusi Berat Produk ({highest_weight_category})")
ax.set_xlabel("Berat Produk (gram)")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

st.sidebar.write("🚀 **Dashboard ini dibuat menggunakan Streamlit**")
