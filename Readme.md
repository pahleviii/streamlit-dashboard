📊 Dashboard Analisis Data dengan Streamlit
Proyek ini merupakan dashboard interaktif yang dikembangkan menggunakan Streamlit untuk melakukan eksplorasi dan visualisasi data. Data yang digunakan berasal dari dataset Olist Orders dan Olist Products.

🎯 Fitur Dashboard
📂 Upload Data: Mengunggah file CSV dan menampilkannya dalam bentuk tabel.
📊 Visualisasi Data: Menampilkan berbagai grafik menggunakan Matplotlib & Seaborn.
🔍 Analisis Statistik: Menyediakan ringkasan statistik dasar dari dataset.
🔄 Interaktif: Memungkinkan filter dan eksplorasi data dengan mudah.
🛠 Instalasi & Menjalankan Dashboard
1️⃣ Clone Repository
git clone https://github.com/USERNAME/streamlit-dashboard.git
cd streamlit-dashboard
2️⃣ Buat Virtual Environment (Opsional, tapi Disarankan)
python -m venv env
source env/bin/activate  # Untuk macOS/Linux
env\Scripts\activate     # Untuk Windows
3️⃣ Install Dependensi
pip install -r requirements.txt
4️⃣ Jalankan Streamlit
streamlit run dashboard.py
📂 Struktur Proyek
streamlit-dashboard/
│── data/                   # Folder untuk menyimpan dataset
│── dashboard.py             # Script utama untuk dashboard Streamlit
│── requirements.txt         # File dependensi Python
│── README.md                # Dokumentasi proyek
📌 Library yang Digunakan
streamlit → Untuk membuat dashboard interaktif
pandas → Untuk manipulasi dan analisis data
matplotlib → Untuk membuat grafik dasar
seaborn → Untuk visualisasi data yang lebih menarik
