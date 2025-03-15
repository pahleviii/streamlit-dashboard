# Dashboard Streamlit untuk Analisis Data

Proyek ini menyediakan **dashboard Streamlit** untuk menganalisis dan memvisualisasikan data produk dari dataset Olist.

## 📌 Fitur
1. **Statistik Deskriptif**: Menampilkan nilai rata-rata, median, standar deviasi, nilai minimum, dan maksimum untuk kolom numerik.
2. **Rata-rata Panjang Deskripsi Produk**: Grafik batang yang menunjukkan hubungan antara jumlah foto produk dan panjang deskripsinya.
3. **Analisis Berat Produk**: Mengidentifikasi kategori dengan berat rata-rata tertinggi dan menampilkan distribusi beratnya.

## 📂 File
- `dashboard.py`: Skrip utama untuk menjalankan dashboard Streamlit.
- `requirements.txt`: Daftar pustaka Python yang dibutuhkan.
- `olist_products_dataset.csv`: Dataset produk.
- `olist_orders_dataset.csv`: Dataset pesanan.

## 🚀 Cara Menjalankan
1. Instal dependensi:
   ```sh
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi Streamlit:
   ```sh
   streamlit run dashboard.py
   ```

## 📊 Informasi Dataset
Dataset ini berisi data terkait produk seperti nama kategori, berat produk, dan panjang deskripsi. Data ini digunakan untuk menghasilkan wawasan dan visualisasi dalam dashboard ini.

## 🛠 Pustaka yang Digunakan
- `pandas` untuk manipulasi data
- `matplotlib` dan `seaborn` untuk visualisasi data
- `streamlit` untuk membangun dashboard interaktif

---
**Dikembangkan dengan ❤️ menggunakan Streamlit.**
