# 📊 Bike Sharing Analysis Dashboard

## 📌 Deskripsi Proyek
Dashboard ini dibuat untuk menganalisis tren peminjaman sepeda berdasarkan dataset **Bike Sharing**. Analisis dilakukan menggunakan **Python**, dengan bantuan library **Pandas, Matplotlib, Seaborn, dan Streamlit**.

## 🔍 Tujuan Analisis
1. **Bagaimana Pola Peminjaman Sepeda Berdasarkan Waktu?**
   - Melihat tren peminjaman sepeda berdasarkan bulan dan jam.
   - Mengidentifikasi kapan peminjaman sepeda paling tinggi dan rendah.
2. **Bagaimana Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda?**
   - Menganalisis bagaimana kondisi cuaca dan musim mempengaruhi jumlah peminjaman sepeda.
   - Memahami apakah cuaca ekstrem berdampak pada jumlah peminjaman.

## 🛠️ Teknologi yang Digunakan
- **Python** (Pandas, Matplotlib, Seaborn, Streamlit)
- **Streamlit** (Untuk membuat dashboard interaktif)

## 📂 Dataset
Dataset yang digunakan terdiri dari dua file utama:
1. `Cleaned_day.csv` → Data harian setelah proses pembersihan.
2. `Cleaned_hour.csv` → Data per jam setelah proses pembersihan.

## 🚀 Cara Menjalankan Dashboard
1. **Pastikan memiliki Python dan Streamlit**
   - Jika belum memiliki Streamlit, instal dengan perintah berikut:
     ```bash
     pip install streamlit pandas matplotlib seaborn
     ```
2. **Jalankan script Streamlit**
   ```bash
   streamlit run dashboard.py
   ```
3. **Buka browser**
   - Streamlit akan membuka dashboard secara otomatis di browser.
   - Jika tidak terbuka, akses secara manual melalui: `http://localhost:8501`

## 📈 Fitur Dashboard
- **Pola Peminjaman Sepeda Berdasarkan Waktu**
  - Grafik rata-rata peminjaman per bulan.
  - Grafik tren peminjaman sepeda per jam.
- **Pengaruh Cuaca terhadap Peminjaman Sepeda**
  - Grafik rata-rata peminjaman berdasarkan musim.
  - Grafik rata-rata peminjaman berdasarkan kondisi cuaca.
- **Fitur interaktif:** Pengguna dapat memilih analisis yang ingin ditampilkan melalui sidebar.

## 📢 Kesimpulan
1. Peminjaman sepeda cenderung **meningkat pada bulan-bulan tertentu**, terutama saat musim semi dan panas.
2. Pola harian menunjukkan bahwa **jam sibuk (morning & evening rush hour) memiliki jumlah peminjaman tertinggi**.
3. Cuaca sangat mempengaruhi jumlah peminjaman. **Hari dengan kondisi cuaca cerah memiliki tingkat peminjaman lebih tinggi dibandingkan hari hujan atau berkabut**.
