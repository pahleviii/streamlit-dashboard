import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
product_df = pd.read_csv("olist_products_dataset.csv")
orders_df = pd.read_csv("olist_orders_dataset.csv")

# Statistik deskriptif
def describe(data):
    numeric_columns = data.select_dtypes(include=['float64', 'int64'])
    stats_df = pd.DataFrame({
        "Mean": numeric_columns.mean(),
        "Median": numeric_columns.median(),
        "Standard Deviation": numeric_columns.std(),
        "Minimum": numeric_columns.min(),
        "Maximum": numeric_columns.max()
    })
    return stats_df

# Sidebar
st.sidebar.header("Dashboard Analisis Data Produk")
option = st.sidebar.selectbox("Pilih Analisis:", ["Statistik Deskriptif", "Rata-rata Deskripsi Produk", "Kategori Berat Produk"])

if option == "Statistik Deskriptif":
    st.header("Statistik Deskriptif Produk")
    stats_summary = describe(product_df)
    st.write(stats_summary)

elif option == "Rata-rata Deskripsi Produk":
    st.header("Rata-rata Panjang Deskripsi Produk Berdasarkan Jumlah Foto")
    kategori = st.selectbox("Pilih Kategori Produk:", product_df["product_category_name"].dropna().unique())
    data_kategori = product_df[product_df["product_category_name"] == kategori]
    avg_description_length = data_kategori.groupby("product_photos_qty")["product_description_lenght"].mean()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_description_length.plot(kind="bar", color="skyblue", ax=ax)
    ax.set_title(f"Rata-rata Panjang Deskripsi Produk ({kategori})")
    ax.set_xlabel("Jumlah Foto Produk")
    ax.set_ylabel("Rata-rata Panjang Deskripsi")
    st.pyplot(fig)

elif option == "Kategori Berat Produk":
    st.header("Kategori dengan Berat Produk Tertinggi")
    avg_weight_per_category = product_df.groupby("product_category_name")["product_weight_g"].mean()
    highest_weight_category = avg_weight_per_category.idxmax()
    highest_weight_value = avg_weight_per_category.max()
    st.write(f"Kategori dengan rata-rata berat tertinggi: **{highest_weight_category} ({highest_weight_value} gram)**")
    
    data_highest_weight = product_df[product_df["product_category_name"] == highest_weight_category]
    fig, ax = plt.subplots(figsize=(10, 6))
    data_highest_weight["product_weight_g"].plot(kind="hist", bins=20, color="orange", alpha=0.7, ax=ax)
    ax.set_title(f"Distribusi Berat Produk ({highest_weight_category})")
    ax.set_xlabel("Berat Produk (gram)")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

st.sidebar.write("Made with ❤️ using Streamlit")
