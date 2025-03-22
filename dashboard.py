import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
Cleaned_day = pd.read_csv("Cleaned_day.csv")
Cleaned_hour = pd.read_csv("Cleaned_hour.csv")

# Dashboard Title
st.title("📊 Dashboard Analisis Peminjaman Sepeda")
st.write("Analisis interaktif berdasarkan dataset Bike Sharing.")

# Sidebar Filter
st.sidebar.header("Filter Data")
view_option = st.sidebar.radio("Pilih Analisis yang Ingin Ditampilkan", ("Pola Peminjaman Berdasarkan Waktu", "Pengaruh Cuaca terhadap Peminjaman"))

if view_option == "Pola Peminjaman Berdasarkan Waktu":
    st.subheader("📅 Pola Peminjaman Sepeda Berdasarkan Waktu")
    
    time_view = st.sidebar.radio("Pilih Tingkat Waktu", ("Bulanan", "Harian"))
    
    if time_view == "Bulanan":
        st.write("### 📆 Rata-rata penyewaan sepeda per bulan")
        monthly_trend = Cleaned_day.groupby("mnth")["cnt"].mean()
        fig, ax = plt.subplots()
        sns.barplot(x=monthly_trend.index, y=monthly_trend.values, palette="coolwarm", ax=ax)
        ax.set_xlabel("Bulan")
        ax.set_ylabel("Jumlah Peminjaman")
        ax.set_title("Rata-rata Peminjaman Sepeda per Bulan")
        st.pyplot(fig)
    
    else:
        st.write("### ⏰ Rata-rata penyewaan sepeda per jam")
        hourly_trend = Cleaned_hour.groupby("hr")["cnt"].mean()
        fig, ax = plt.subplots()
        sns.lineplot(x=hourly_trend.index, y=hourly_trend.values, marker='o', ax=ax)
        ax.set_xlabel("Jam")
        ax.set_ylabel("Jumlah Peminjaman")
        ax.set_title("Tren Peminjaman Sepeda per Jam")
        st.pyplot(fig)

elif view_option == "Pengaruh Cuaca terhadap Peminjaman":
    st.subheader("🌤️ Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda")
    
    weather_view = st.sidebar.radio("Pilih Faktor Cuaca", ("Musim", "Kondisi Cuaca"))
    
    if weather_view == "Musim":
        st.write("### 🌍 Rata-rata penyewaan sepeda berdasarkan musim")
        season_trend = Cleaned_day.groupby("season")["cnt"].mean()
        fig, ax = plt.subplots()
        sns.barplot(x=season_trend.index, y=season_trend.values, palette="viridis", ax=ax)
        ax.set_xlabel("Musim")
        ax.set_ylabel("Jumlah Peminjaman")
        ax.set_title("Rata-rata Peminjaman Sepeda per Musim")
        st.pyplot(fig)
    
    else:
        st.write("### ☁️ Rata-rata penyewaan sepeda berdasarkan kondisi cuaca")
        weather_trend = Cleaned_hour.groupby("weathersit")["cnt"].mean()
        fig, ax = plt.subplots()
        sns.barplot(x=weather_trend.index, y=weather_trend.values, palette="magma", ax=ax)
        ax.set_xlabel("Kondisi Cuaca")
        ax.set_ylabel("Jumlah Peminjaman")
        ax.set_title("Rata-rata Peminjaman Sepeda per Kondisi Cuaca")
        st.pyplot(fig)

st.write("---")
st.write("📌 Dashboard ini dibuat menggunakan Streamlit untuk menampilkan hasil analisis data secara interaktif sesuai dengan pertanyaan penelitian.")