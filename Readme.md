# 📊 Dashboard Analisis Peminjaman Sepeda

## 📌 Deskripsi Proyek
Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis pola peminjaman sepeda berdasarkan dataset yang telah dibersihkan. Dashboard ini memungkinkan pengguna untuk memahami bagaimana pola peminjaman sepeda berubah berdasarkan waktu dan kondisi cuaca melalui visualisasi yang interaktif.

## 🛠 Fitur Utama
✅ **Filter Rentang Tanggal** – Memungkinkan pengguna memilih tanggal tertentu untuk dianalisis.
✅ **Filter Musim & Cuaca** – Analisis berdasarkan musim dan kondisi cuaca tertentu.
✅ **Filter Jam Operasional** – Memilih rentang jam untuk melihat pola peminjaman sepeda.
✅ **Visualisasi Dinamis** – Grafik diperbarui secara otomatis berdasarkan filter yang dipilih.
✅ **Tampilan Data Hasil Filter** – Menampilkan data yang sudah difilter secara langsung di bawah visualisasi.

## 🔎 Pertanyaan Analisis
1️⃣ **Bagaimana Pola Peminjaman Sepeda Berdasarkan Waktu?**  
   - Melalui grafik peminjaman per hari dalam seminggu.
   - Melalui grafik peminjaman per jam dalam sehari.

2️⃣ **Bagaimana Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda?**  
   - Melalui analisis jumlah peminjaman berdasarkan kondisi cuaca.

## 📂 Dataset
Dataset yang digunakan berasal dari **Cleaned_day.csv** dan **Cleaned_hour.csv**, yang telah melalui tahap pembersihan dan transformasi data.

## 🚀 Cara Menjalankan Dashboard
1️⃣ Pastikan Anda telah menginstall semua dependensi yang dibutuhkan:
```bash
pip install streamlit pandas matplotlib seaborn
```

2️⃣ Jalankan aplikasi dengan perintah berikut:
```bash
streamlit run dashboard.py
```

3️⃣ Dashboard akan terbuka secara otomatis di browser dan siap digunakan.

## 📊 Visualisasi yang Ditampilkan
- **Grafik Pola Peminjaman Sepeda per Hari dalam Seminggu**  
- **Grafik Pola Peminjaman Sepeda per Jam dalam Sehari**  
- **Grafik Jumlah Peminjaman Berdasarkan Cuaca**  

## 💡 Insight dari Analisis
🔹 Peminjaman sepeda cenderung meningkat pada hari kerja dibandingkan akhir pekan.  
🔹 Peminjaman sepeda lebih tinggi pada jam sibuk (pagi & sore).  
🔹 Kondisi cuaca yang buruk menyebabkan jumlah peminjaman menurun secara signifikan.  

## 🏗 Pengembangan Selanjutnya
🚀 Menambahkan lebih banyak fitur interaktif seperti filter berdasarkan hari kerja atau akhir pekan.
🚀 Implementasi model prediksi jumlah peminjaman sepeda berdasarkan cuaca dan waktu.

---
✨ **Dibuat dengan ❤️ menggunakan Streamlit, Pandas, Matplotlib, dan Seaborn** ✨

