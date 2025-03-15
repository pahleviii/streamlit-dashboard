import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


product_df = pd.read_csv("F:/Tugas/Studi Independen/Proyek analisis data/dashboard/olist_products_dataset.csv")
orders_df = pd.read_csv("F:/Tugas/Studi Independen/Proyek analisis data/dashboard/olist_orders_dataset.csv")

new_order_df = pd.merge(
    left=product_df,
    right=orders_df,
    how="inner",
    left_on="product_id",
    right_on="order_id"
)


product_df = pd.read_csv("F:/Tugas/Studi Independen/Proyek analisis data/dashboard/olist_products_dataset.csv")

product_df.isnull().sum()


products_df = pd.read_csv("F:/Tugas/Studi Independen/Proyek analisis data/dashboard/olist_products_dataset.csv")

products_df.dropna(axis=0, inplace=True)




# Muat dataset
file_path = "F:/Tugas/Studi Independen/Proyek analisis data/dashboard/olist_products_dataset.csv"
data = pd.read_csv("F:/Tugas/Studi Independen/Proyek analisis data/dashboard/olist_products_dataset.csv")

# Method describe() untuk eksplorasi parameter statistik
def describe(data):
    """
    Menghitung statistik deskriptif untuk kolom numerik dalam dataset.
    """
    # Pilih hanya kolom numerik
    numeric_columns = data.select_dtypes(include=['float64', 'int64'])

    # Hitung statistik deskriptif
    stats = {
        "Mean": numeric_columns.mean(),
        "Median": numeric_columns.median(),
        "Standard Deviation": numeric_columns.std(),
        "Minimum": numeric_columns.min(),
        "Maximum": numeric_columns.max()
    }

    # Konversi hasil ke DataFrame untuk tampilan yang lebih baik
    stats_df = pd.DataFrame(stats)

    return stats_df

# Panggil method describe() dan cetak hasilnya
stats_summary = describe(data)
print(stats_summary)

data = pd.read_csv("F:/Tugas/Studi Independen/Proyek analisis data/dashboard/olist_products_dataset.csv")
# Filter data untuk kategori tertentu (contoh: 'bebes')
kategori = "bebes"
data_kategori = data[data["product_category_name"] == kategori]

# Hitung rata-rata panjang deskripsi berdasarkan jumlah foto
avg_description_length = data_kategori.groupby("product_photos_qty")["product_description_lenght"].mean()

# Visualisasi hasil
plt.figure(figsize=(10, 6))
avg_description_length.plot(kind="bar", color="skyblue")
plt.title(f"Rata-rata Panjang Deskripsi Produk Berdasarkan Jumlah Foto ({kategori})")
plt.xlabel("Jumlah Foto Produk")
plt.ylabel("Rata-rata Panjang Deskripsi")
plt.xticks(rotation=0)
plt.show()

"""### Pertanyaan 2:"""

# Hitung rata-rata berat produk per kategori
avg_weight_per_category = data.groupby("product_category_name")["product_weight_g"].mean()

# Identifikasi kategori dengan rata-rata berat tertinggi
highest_weight_category = avg_weight_per_category.idxmax()
highest_weight_value = avg_weight_per_category.max()
print(f"Kategori dengan rata-rata berat tertinggi: {highest_weight_category} ({highest_weight_value} gram)")

# Filter data untuk kategori dengan berat tertinggi
data_highest_weight = data[data["product_category_name"] == highest_weight_category]

# Analisis distribusi berat produk dalam kategori tersebut
plt.figure(figsize=(10, 6))
data_highest_weight["product_weight_g"].plot(kind="hist", bins=20, color="orange", alpha=0.7)
plt.title(f"Distribusi Berat Produk ({highest_weight_category})")
plt.xlabel("Berat Produk (gram)")
plt.ylabel("Frekuensi")
plt.show()
