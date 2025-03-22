import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned datasets
Cleaned_day = pd.read_csv("Cleaned_day.csv")
Cleaned_hour = pd.read_csv("Cleaned_hour.csv")

# Konversi kolom tanggal menjadi datetime
Cleaned_day["dteday"] = pd.to_datetime(Cleaned_day["dteday"])
Cleaned_hour["dteday"] = pd.to_datetime(Cleaned_hour["dteday"])

# Streamlit Title
st.title("📊 Dashboard Analisis Peminjaman Sepeda")

# --- **Fitur Interaktif: Rentang Tanggal** ---
st.sidebar.header("📅 Filter Data")
start_date = st.sidebar.date_input("Mulai", value=Cleaned_day["dteday"].min())
end_date = st.sidebar.date_input("Akhir", value=Cleaned_day["dteday"].max())

# Filter dataset berdasarkan tanggal yang dipilih
filtered_day = Cleaned_day[(Cleaned_day["dteday"] >= pd.to_datetime(start_date)) & (Cleaned_day["dteday"] <= pd.to_datetime(end_date))]
filtered_hour = Cleaned_hour[(Cleaned_hour["dteday"] >= pd.to_datetime(start_date)) & (Cleaned_hour["dteday"] <= pd.to_datetime(end_date))]

# --- **Fitur Interaktif: Pilihan Filter Lanjutan** ---
season_filter = st.sidebar.selectbox("🌤 Pilih Musim:", filtered_day["season"].unique())
weather_filter = st.sidebar.selectbox("☁️ Pilih Kondisi Cuaca:", filtered_hour["weathersit"].unique())
hour_filter = st.sidebar.slider("🕒 Pilih Rentang Jam:", 0, 23, (6, 18))  # Default 6 AM - 6 PM

# Filter dataset berdasarkan pilihan user
filtered_day = filtered_day[filtered_day["season"] == season_filter]
filtered_hour = filtered_hour[(filtered_hour["weathersit"] == weather_filter) & 
                              (filtered_hour["hr"] >= hour_filter[0]) & 
                              (filtered_hour["hr"] <= hour_filter[1])]

# --- **Visualisasi 1: Pola Peminjaman Sepeda Berdasarkan Waktu** ---
st.subheader("📅 Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=filtered_day, x="weekday", y="cnt", palette="coolwarm", ci=None, ax=ax)
ax.set_title("Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu")
ax.set_xlabel("Hari dalam Minggu (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Rata-rata Jumlah Peminjaman")
st.pyplot(fig)

# --- **Visualisasi 2: Pola Peminjaman Sepeda per Jam** ---
st.subheader("⏰ Pola Peminjaman Sepeda Berdasarkan Jam dalam Sehari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_hour, x="hr", y="cnt", marker="o", ax=ax, color="blue")
ax.set_title("Rata-rata Peminjaman Sepeda per Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# --- **Visualisasi 3: Pengaruh Cuaca terhadap Peminjaman Sepeda** ---
st.subheader("☁️ Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=filtered_hour, x="weathersit", y="cnt", estimator=sum, ci=None, ax=ax, palette="Blues")
ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Cuaca")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

# --- **Tampilkan Data yang Sudah Difilter** ---
st.subheader("📜 Data Peminjaman Sepeda Setelah Difilter")
st.write(filtered_hour)
