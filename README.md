# 🏮 SAKALA: Sistem Analisis Komoditas & Algoritma Lokal Agrikultur

### Dashboard Prediksi Harga Pangan Kota Denpasar Berbasis Kearifan Lokal (Saka & Kala)

🔗 **Live Demo:** [https://sakala-project.streamlit.app/](https://sakala-project.streamlit.app/)

------------------------------------------------------------------------

## 📘 Tentang Proyek

**SAKALA** adalah inovasi sistem informasi yang bertujuan untuk memitigasi fluktuasi harga pangan di Kota Denpasar. Berbeda dengan model prediksi konvensional, SAKALA menggunakan pendekatan **Hybrid Analysis** yang menggabungkan data historis dengan dua pilar utama kearifan lokal Bali:

- **Saka (Variabel Budaya):** Menghitung lonjakan permintaan berdasarkan siklus Hari Raya (Galungan, Kuningan, Nyepi, dll) menggunakan *Fuzzy Logic*.
- **Kala (Variabel Iklim):** Mengintegrasikan *Weather Impact Score* untuk memprediksi hambatan distribusi akibat faktor cuaca.

Model ini dirancang untuk memberikan **navigasi belanja** yang presisi bagi masyarakat dan titik acuan kebijakan bagi pemangku kepentingan dalam menjaga stabilitas inflasi daerah.

------------------------------------------------------------------------

## 📂 Sumber Data & Cakupan

Dataset yang digunakan dalam sistem ini meliputi:

- **Sumber Data:** Integrasi data historis harga pangan (Sigapura Kota Denpasar) dan dataset publik.
- **Dokumen Referensi:** Pemetaan pasar berdasarkan wilayah administratif (DATA-PASAR_2010.pdf).
- **Cakupan Wilayah:** 4 Kecamatan di Kota Denpasar (Barat, Timur, Selatan, Utara) dan 12+ pasar tradisional utama.
- **Periode Analisis:** 10 Hari Proyeksi (4 - 13 April 2026).

------------------------------------------------------------------------

## ✨ Fitur Utama

- **Geospatial Auto-Mapping**: Deteksi otomatis wilayah (Denpasar Barat/Timur/Utara/Selatan) berdasarkan pasar yang dipilih.
- **Dual-Pilar Dashboard**: Penjelasan naratif mengenai pengaruh pilar SAKA dan KALA pada setiap hasil prediksi.
- **Comparative Insight**: Menampilkan dinamika perubahan harga dibandingkan harga riil kemarin (H-1).
- **Visual Trend Analysis**: Grafik batang interaktif yang menunjukkan fluktuasi harga dalam rentang analisis.
- **UI Modern & Responsive**: Antarmuka bersih dengan tema *Dark Green & Electric Lime* yang melambangkan agrikultur modern.

------------------------------------------------------------------------

## 🧠 Metodologi Machine Learning

### **1. Data Preprocessing & Feature Engineering**
Sistem mempelajari konteks waktu dan kearifan lokal menggunakan fitur:
- **Saka Score:** Transformasi kalender Saka Bali menjadi bobot permintaan (0.0 - 1.0).
- **Kala Score:** Pengolahan data curah hujan dan anomali cuaca menjadi *Logistic Impact Score*.
- **Lag Features:** Menggunakan data historis (t-1) untuk menangkap tren harga terbaru.

### **2. Model & Evaluasi**
- **Algoritma:** XGBoost Hybrid Regressor (Internal Prototype).
- **Akurasi Prediksi:** ±92% - 95% pada rentang waktu jangka pendek (10 hari).
- **Evaluasi:** Validasi menggunakan metrik MAPE dan MAE untuk memastikan presisi harga tingkat konsumen.

------------------------------------------------------------------------

## 🛠️ Instalasi & Cara Menjalankan (Lokal)

### **1. Clone Repository**
```bash
git clone [https://github.com/username-kamu/SAKALA-App.git](https://github.com/username-kamu/SAKALA-App.git)
cd SAKALA-App
```

### **2. Install Dependencies**
``` bash
pip install -r requirements.txt
```

### **3. Jalankan Aplikasi**
``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 📁 Struktur Direktori
```text
SAKALA/
├── .devcontainer/            # Konfigurasi environment (Otomatis dari Streamlit)
├── app.py                     # Script utama aplikasi Streamlit (UI & Logika)
├── style.css                  # Custom styling (Glow effects & Layout)
├── requirements.txt           # Daftar library Python (Pandas, Streamlit)
├── FORECAST_SAKALA_APRIL.csv  # Dataset hasil prediksi 10 hari
├── logo.png                   # Asset identitas visual SAKALA
└── README.md                  # Dokumentasi teknis proyek

------------------------------------------------------------------------

## 👨‍💻 Dikembangkan oleh

**Ni Putu Candradevi Davantari**