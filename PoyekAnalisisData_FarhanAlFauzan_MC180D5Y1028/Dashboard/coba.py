import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='dark')


st.title("Proyek Analisis Data Farhan Al Fauzan")

st.header('Data Tabel Pelanggan')
pelanggan = pd.read_csv(r'D:\Dokumen Farhan\Semester 6\DBS Foundation\PoyekAnalisisData_FarhanAlFauzan_MC180D5Y1028\Dashboard\customers_dataset.csv')
st.dataframe (pelanggan, width=1000, height=400)


# Membuat plot untuk Kota Dengan Pesanan Terbanyak
st.header('Top 10 Kota Dengan Jumlah Pelanggan Terbanyak')
jumlah_kota = pelanggan['customer_city'].value_counts().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=jumlah_kota.index, y=jumlah_kota.values, ax=ax)
ax.set_title('Top 10 Kota Dengan Jumlah Pelanggan Terbanyak')
ax.set_xlabel('Kota')
ax.set_ylabel('Jumlah Pelanggan')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig)

st.header('Data Tabel Produk')
produk = pd.read_csv(r'D:\Dokumen Farhan\Semester 6\DBS Foundation\PoyekAnalisisData_FarhanAlFauzan_MC180D5Y1028\Dashboard\products_dataset.csv')
st.dataframe (pelanggan, width=1000, height=400)

# Plot Kategori Produk Terlaris
st.header('Top 10 Kategori Produk Terlaris')
produk.fillna(value='cama_mesa_banho', inplace=True)  # Handle missing values
jumlah_produk = produk['product_category_name'].value_counts().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=jumlah_produk.index, y=jumlah_produk.values, ax=ax2)
ax2.set_title('Top 10 Kategori Produk Dengan Tingkat Penjualan Terbanyak')
ax2.set_xlabel('Kategori Produk')
ax2.set_ylabel('Jumlah Pesanan')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig2)