import streamlit as st
import pandas as pd
import os
import base64
from datetime import timedelta

# 1. SETUP PAGE
st.set_page_config(page_title="SAKALA", layout="wide")

def load_css():
    if os.path.exists("style.css"):
        with open("style.css") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
load_css()

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# 2. LOAD DATA
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("FORECAST_SAKALA_APRIL.csv")
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])
        return df
    except:
        return pd.DataFrame()

df = load_data()

# 3. HERO SECTION
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">SAKALA</h1>
        <p style="font-size:18px; opacity:0.9;">Sistem Analisis Komoditas dan Algoritma Lokal Agrikultur</p>
    </div>
""", unsafe_allow_html=True)

# 4. KONFIGURASI ANALISIS
if not df.empty:
    st.markdown('<div style="background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.05);">', unsafe_allow_html=True)
    st.markdown("### 🔍 Konfigurasi Analisis")
    
    col_1, col_2 = st.columns(2)
    with col_1:
        # 1. Mengambil SELURUH pasar dari dataset
        daftar_semua_pasar = sorted(df['Pasar'].unique())
        pasar_pilihan = st.selectbox("Pilih Pasar Tujuan:", daftar_semua_pasar)
        
        # 2. Mapping Wilayah
        wilayah_map = {
            # PUSAT KOTA
            'Kota Denpasar': 'Pusat Kota', 

            # DENPASAR BARAT
            'Pasar Badung': 'Denpasar Barat', 
            'Pasar Sanglah': 'Denpasar Barat',
            'Pasar Padangsambian': 'Denpasar Barat',

            # DENPASAR TIMUR
            'Pasar Kreneng': 'Denpasar Timur', 
            'Pasar Asoka Kreneng': 'Denpasar Timur',
            'PASAR KETAPIAN': 'Denpasar Timur', 
            'Pasar Satriya': 'Denpasar Timur',
            'Pasar Penatih': 'Denpasar Timur',

            # DENPASAR SELATAN
            'PASAR NYANGGELAN': 'Denpasar Selatan', 

            # DENPASAR UTARA
            'Pasar Agung Peninjoan': 'Denpasar Utara',
            'Pasar Kreneng': 'Denpasar Utara',
        }

        # 3. Menampilkan Wilayah secara otomatis berdasarkan pilihan pasar
        wilayah_terdeteksi = wilayah_map.get(pasar_pilihan, "Wilayah tidak terdaftar")
        st.info(f"📍 Wilayah Terdeteksi: **{wilayah_terdeteksi}**")

    with col_2:
        komoditas_pilihan = st.selectbox("🌶️ Pilih Bahan Pangan:", df['Komoditas'].unique())
        
        # LOGIKA RENTANG 10 HARI 
        data_min = df['Tanggal'].min() 
        default_date = data_min + timedelta(days=1)
        end_limit = data_min + timedelta(days=9) 
        
        tanggal_pilihan = st.date_input(
            "📆 Pilih Tanggal Analisis:", 
            value=default_date,
            min_value=data_min,
            max_value=end_limit
        )

    btn_hitung = st.button("🔮 Hitung prediksi")
    st.markdown('</div>', unsafe_allow_html=True)

    # 5. HASIL & NARASI SAINS
    if btn_hitung:
        df_filtered = df[(df['Komoditas'] == komoditas_pilihan) & (df['Pasar'] == pasar_pilihan)].sort_values('Tanggal')
        res_target = df_filtered[df_filtered['Tanggal'] == pd.to_datetime(tanggal_pilihan)]
        tgl_kemarin = pd.to_datetime(tanggal_pilihan) - timedelta(days=1)
        res_riil = df_filtered[df_filtered['Tanggal'] == tgl_kemarin]

        if not res_target.empty:
            target = res_target.iloc[0]
            
            st.markdown(f"""
            <div style="background:#1B4D3E; padding:25px; border-radius:20px 20px 0 0; text-align:center; color:white;">
                <h3 style="margin:0;">HASIL PREDIKSI SAKALA</h3>
                <p style="margin:5px 0; opacity:0.8; font-size:16px;">
                    {komoditas_pilihan} | {pasar_pilihan} | {tanggal_pilihan.strftime('%d %B %Y')}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f'<div style="background:white; padding:30px; text-align:center; border:1px solid #EEE;"><h1 style="font-size:60px; color:#1B4D3E; margin:0;">Rp {int(target["Prediksi"]):,}<span style="font-size:20px; color:#5F7A61;"> / kg</span></h1></div>', unsafe_allow_html=True)
            
            # KOMPARASI 
            col_r1, col_r2 = st.columns(2)
            if not res_riil.empty:
                h_riil = res_riil.iloc[0]['Prediksi']
                selisih = target['Prediksi'] - h_riil
                stat = "Meningkat" if selisih > 0 else "Menurun/Stabil"
                
                with col_r1:
                    st.markdown(f'<div class="highlight-box"><small>Harga Kemarin (Riil)</small><br><span style="font-size:22px;">Rp {int(h_riil):,}</span></div>', unsafe_allow_html=True)
                with col_r2:
                    st.markdown(f'<div class="highlight-box"><small>Dinamika Harga (vs Kemarin)</small><br><span style="font-size:22px;">{stat} (Rp {abs(int(selisih)):,})</span></div>', unsafe_allow_html=True)
            else:
                with col_r1:
                    st.markdown(f'<div class="highlight-box"><small>Info Harga</small><br><span style="font-size:22px;">Data Baseline</span></div>', unsafe_allow_html=True)
                with col_r2:
                    st.markdown(f'<div class="highlight-box"><small>Status</small><br><span style="font-size:18px;">Awal Periode Analisis</span></div>', unsafe_allow_html=True)

            st.write("<br>", unsafe_allow_html=True)
            st.markdown("### 🧬 Dasar Pertimbangan Algoritma")
            
            c_saka, c_kala = st.columns(2)
            with c_saka:
                impact_saka = int(target['skor_saka_fuzzy'] * 100)
                narasi_saka = f"Sistem mendeteksi pengaruh variabel **Budaya (Saka)** sebesar {impact_saka}%. "
                if impact_saka > 50:
                    narasi_saka += "Hal ini dikarenakan adanya persiapan **Hari Raya besar di Bali** yang memicu lonjakan permintaan pasar."
                else:
                    narasi_saka += "Kondisi permintaan stabil karena berada dalam periode hari biasa (Nitya)."
                st.info(f"📆 **Pilar SAKA:** {narasi_saka}")

            with c_kala:
                weather_val = target['weather_impact_score']
                narasi_kala = "Analisis **Waktu & Iklim (Kala)** menunjukkan bahwa "
                if weather_val > 15:
                    narasi_kala += f"curah hujan tinggi/cuaca buruk di jalur distribusi (Skor: {int(weather_val)}) berpotensi menghambat pasokan barang."
                else:
                    narasi_kala += "kondisi cuaca terpantau cerah dan siklus panen lancar, mendukung stabilitas distribusi."
                st.success(f"⏳ **Pilar KALA:** {narasi_kala}")

            st.write("---")
            st.write(f"### 📊 Tren Mingguan Harga {komoditas_pilihan} di {pasar_pilihan}")
            df_chart = df_filtered.tail(7).copy()
            df_chart['Tanggal'] = df_chart['Tanggal'].dt.strftime('%d %b')
            st.bar_chart(df_chart.set_index('Tanggal')['Prediksi'], color="#C5A065")
            
            # TABEL TREN 
            df_display = df_chart[['Tanggal', 'Prediksi']].set_index('Tanggal')
            st.table(df_display.style.format("Rp {:,.0f}"))

# FOOTER
logo_b64 = get_base64_image("logo.png")
st.markdown("---")
st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center; gap:20px; padding:30px;">
        <img src="data:image/png;base64,{logo_b64}" class="footer-logo">
        <div style="text-align:left; border-left:2px solid #C5A065; padding-left:15px;">
            <b style="color:#1B4D3E; font-size:20px;">SAKALA 2026</b><br>
            <span style="font-size:14px;">Sistem Analisis Komoditas dan Algoritma Lokal Agrikultur</span>
        </div>
    </div>
""", unsafe_allow_html=True)