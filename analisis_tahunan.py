#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏦 BNI Strategic Intelligence: Analisis Realisasi Investasi Indonesia Tahun 2025
-------------------------------------------------------------------------
Deskripsi: Script ini menggabungkan dan menganalisis data realisasi investasi 
           Triwulan I s/d IV Tahun 2025 untuk memberikan panduan intelijen bisnis 
           tingkat tinggi (high-level) bagi Branch Manager & Relationship Manager (RM).
           
Dibuat oleh: Antigravity AI Assistant
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- KONFIGURASI ESTETIKA PREMIUM ---
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.titlepad'] = 20
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

# Palet warna premium BNI (Deep Blue, Teal, & Warm Orange)
PALETTE_BNI_DARK = "#005E7C"  # Teal Khas BNI
PALETTE_BNI_ORANGE = "#F15A24" # Orange Aksen BNI
PALETTE_NEUTRAL_DARK = "#2B2D42"

def main():
    print("=" * 70)
    print(" 🏦 BNI STRATEGIC INVESTASI - TAHUNAN 2025 ")
    print("=" * 70)
    
    # 1. Verifikasi File Data
    csv_files = [
        'Data Realisasi Investasi Triwulan I Tahun 2025.csv',
        'Data Realisasi Investasi Triwulan II Tahun 2025.csv',
        'Data Realisasi Investasi Triwulan III Tahun 2025.csv',
        'Data Realisasi Investasi Triwulan IV Tahun 2025.csv'
    ]
    
    for f in csv_files:
        if not os.path.exists(f):
            print(f"❌ Error: File '{f}' tidak ditemukan di direktori saat ini.")
            print("Pastikan Anda menjalankan script ini dari root project.")
            return

    # Create outputs folder if not exists
    os.makedirs('outputs', exist_ok=True)
    print("✓ Membuat/verifikasi direktori 'outputs'...")

    # 2. Loading & Pembersihan Data
    print("✓ Memuat dan memproses data dari Triwulan I s/d IV...")
    dfs = []
    for i, file_name in enumerate(csv_files):
        df = pd.read_csv(file_name)
        # Standarisasi tipe data numerik
        df['investasi_rp_juta'] = pd.to_numeric(df['investasi_rp_juta'], errors='coerce').fillna(0)
        df['investasi_us_ribu'] = pd.to_numeric(df['investasi_us_ribu'], errors='coerce').fillna(0)
        df['tki'] = pd.to_numeric(df['tki'], errors='coerce').fillna(0)
        df['quarter'] = f"Q{i+1}"
        dfs.append(df)
        
    df_all = pd.concat(dfs, ignore_index=True)
    
    # 3. Analisis & Output Teks Strategis
    total_rp_triliun = df_all['investasi_rp_juta'].sum() / 1e6
    total_us_juta = df_all['investasi_us_ribu'].sum() / 1e3
    total_tki = df_all['tki'].sum()
    total_projects = len(df_all)
    
    print("\n" + "=" * 50)
    print(" 📊 RINGKASAN DATA TAHUNAN 2025")
    print("=" * 50)
    print(f"• Total Investasi Tahunan      : Rp {total_rp_triliun:,.2f} Triliun (USD {total_us_juta:,.2f} Juta)")
    print(f"• Total Penyerapan Tenaga Kerja: {total_tki:,.0f} orang")
    print(f"• Total Proyek Investasi       : {total_projects:,.0f} proyek")
    
    print("\n" + "-" * 50)
    print(" 📈 TREN PENINGKATAN PER KUARTAL")
    print("-" * 50)
    summary_q = df_all.groupby('quarter').agg(
        total_investasi_rp_triliun=('investasi_rp_juta', lambda x: x.sum() / 1e6),
        total_tki=('tki', 'sum'),
        jumlah_proyek=('periode', 'count')
    )
    for q, row in summary_q.iterrows():
        print(f"• {q}: Rp {row['total_investasi_rp_triliun']:,.2f} Triliun | Penyerapan TKI: {row['total_tki']:,.0f} orang | {row['jumlah_proyek']:,.0f} Proyek")
        
    # 4. Pembuatan Visualisasi Premium
    print("\n" + "✓ Membuat visualisasi premium...")

    # Chart 1: Tren Realisasi Investasi & Penyerapan TKI Per Kuartal
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Bar Chart untuk Investasi
    bars = ax1.bar(summary_q.index, summary_q['total_investasi_rp_triliun'], color=PALETTE_BNI_DARK, width=0.4, label='Investasi (Rp Triliun)', alpha=0.9)
    ax1.set_xlabel('Kuartal 2025', fontweight='bold', labelpad=10)
    ax1.set_ylabel('Nilai Investasi (Rp Triliun)', color=PALETTE_BNI_DARK, fontweight='bold', labelpad=10)
    ax1.tick_params(axis='y', labelcolor=PALETTE_BNI_DARK)
    ax1.set_ylim(0, 550)
    
    # Menambahkan label nilai di atas bar
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f"Rp {yval:,.1f} T", ha='center', va='bottom', color=PALETTE_NEUTRAL_DARK, fontweight='bold', fontsize=10)

    # Line Chart untuk TKI (Axis Kanan)
    ax2 = ax1.twinx()
    line = ax2.plot(summary_q.index, summary_q['total_tki'] / 1000, color=PALETTE_BNI_ORANGE, marker='o', linewidth=3, markersize=8, label='Penyerapan TKI (Ribu Orang)')
    ax2.set_ylabel('Penyerapan TKI (Ribu Orang)', color=PALETTE_BNI_ORANGE, fontweight='bold', labelpad=10)
    ax2.tick_params(axis='y', labelcolor=PALETTE_BNI_ORANGE)
    ax2.set_ylim(0, 850)
    
    # Menambahkan label nilai di atas titik line
    for i, txt in enumerate(summary_q['total_tki'] / 1000):
        ax2.annotate(f"{txt:,.0f}K", (summary_q.index[i], txt + 20), ha='center', va='bottom', color=PALETTE_BNI_ORANGE, fontweight='bold', fontsize=10)

    plt.title('Tren Realisasi Investasi & Penyerapan TKI (Q1 - Q4 2025)', fontsize=15, pad=20, fontweight='bold', color=PALETTE_NEUTRAL_DARK)
    fig.tight_layout()
    plt.savefig('outputs/01_tren_investasi_tki_2025.png', dpi=300)
    plt.close()

    # Chart 2: Top 10 Provinsi (Prioritas Sumber Daya Bank)
    plt.figure(figsize=(12, 7))
    top_prov = df_all.groupby('provinsi')['investasi_rp_juta'].sum().sort_values(ascending=False).head(10) / 1e6
    colors = sns.color_palette("Blues_r", len(top_prov))
    sns.barplot(x=top_prov.values, y=top_prov.index, hue=top_prov.index, palette=colors, legend=False)
    plt.title('Top 10 Provinsi: Prioritas Alokasi Sumber Daya BNI 2025', fontweight='bold', pad=15)
    plt.xlabel('Total Realisasi Investasi (Rp Triliun)', fontweight='bold')
    plt.ylabel('Provinsi', fontweight='bold')
    
    for i, v in enumerate(top_prov.values):
        plt.text(v + 5, i, f"Rp {v:,.1f} T", va='center', fontweight='bold', color=PALETTE_NEUTRAL_DARK, fontsize=9)
        
    plt.tight_layout()
    plt.savefig('outputs/02_top_10_provinsi_2025.png', dpi=300)
    plt.close()

    # Chart 3: Top 10 Sektor Industri Terpanas (Target Nasabah Korporat)
    plt.figure(figsize=(12, 8))
    top_sect = df_all.groupby('nama_sektor')['investasi_rp_juta'].sum().sort_values(ascending=False).head(10) / 1e6
    sns.barplot(x=top_sect.values, y=top_sect.index, hue=top_sect.index, palette=[PALETTE_BNI_DARK] * len(top_sect), legend=False)
    plt.title('Top 10 Sektor Industri Terpanas (Target Portofolio Kredit 2025)', fontweight='bold', pad=15)
    plt.xlabel('Total Realisasi Investasi (Rp Triliun)', fontweight='bold')
    plt.ylabel('Sektor Industri', fontweight='bold')
    
    for i, v in enumerate(top_sect.values):
        plt.text(v + 3, i, f"Rp {v:,.1f} T", va='center', fontweight='bold', color=PALETTE_NEUTRAL_DARK, fontsize=9)
        
    plt.tight_layout()
    plt.savefig('outputs/03_top_10_sektor_2025.png', dpi=300)
    plt.close()

    # Chart 4: Distribusi Jawa vs Luar Jawa
    plt.figure(figsize=(8, 6))
    jawa_vs_luar = df_all.groupby('jawa_luar_jawa')['investasi_rp_juta'].sum()
    labels = jawa_vs_luar.index
    sizes = jawa_vs_luar.values
    colors_pie = [PALETTE_BNI_DARK, PALETTE_BNI_ORANGE]
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors_pie, 
            textprops={'fontsize': 12, 'weight': 'bold'}, wedgeprops=dict(width=0.4, edgecolor='w'))
    
    plt.title('Distribusi Kewilayahan Investasi (Jawa vs Luar Jawa 2025)', fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('outputs/04_distribusi_jawa_luar_jawa_2025.png', dpi=300)
    plt.close()

    print("\n" + "=" * 50)
    print(" 🎉 PROSES ANALISIS & VISUALISASI BERHASIL!")
    print("=" * 50)
    print("Grafik premium berikut telah disimpan di folder 'outputs/':")
    print(" 📂 outputs/01_tren_investasi_tki_2025.png      -> Tren Triwulanan")
    print(" 📂 outputs/02_top_10_provinsi_2025.png         -> Provinsi Target Utama")
    print(" 📂 outputs/03_top_10_sektor_2025.png           -> Sektor Target Kredit")
    print(" 📂 outputs/04_distribusi_jawa_luar_jawa_2025.png -> Distribusi Wilayah")
    print("=" * 50)
    
if __name__ == "__main__":
    main()
