# 🏦 Analisis Realisasi Investasi Indonesia 2025

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Repositori ini berisi alat bantu analisis bisnis tingkat tinggi (**Strategic Business Intelligence**) yang dirancang khusus untuk membantu **Branch Manager, Relationship Manager (RM), & Tim Risiko Kredit** di Bank BNI dalam memetakan peluang penyaluran kredit korporat, *payroll*, dan ekspansi jaringan kantor cabang berdasarkan data realisasi investasi resmi di Indonesia selama tahun 2025.

---

## 📌 Daftar Isi
- [Latar Belakang](#-latar-belakang)
- [Struktur Proyek](#%EF%B8%8F-struktur-proyek)
- [Struktur Data (CSV)](#-struktur-data-csv)
- [Hasil Analisis Strategis Tahunan 2025](#-hasil-analisis-strategis-tahunan-2025)
  - [Ringkasan Utama](#1-ringkasan-utama-2025)
  - [Tren Realisasi per Kuartal](#2-tren-realisasi-per-kuartal)
  - [Top 5 Provinsi Prioritas](#3-top-5-provinsi-prioritas-bni)
  - [Top 5 Sektor Terpanas](#4-top-5-sektor-terpanas-target-kredit)
  - [Keseimbangan Kewilayahan](#5-keseimbangan-kewilayahan-jawa-vs-luar-jawa)
- [Instalasi & Panduan Menjalankan](#-instalasi--panduan-menjalankan)
- [Panduan Push ke GitHub](#-panduan-push-ke-github)

---

## 🏢 Latar Belakang

Memahami realisasi investasi bukan sekadar membaca angka triliunan Rupiah, melainkan memetakan **peluang dan risiko bisnis perbankan**. 
* **Peluang Likuiditas & Payroll:** Daerah dengan realisasi investasi padat karya yang tinggi adalah "kolam" nasabah retail, payroll, *Consumer Lending* (KPR, KKB), serta kartu kredit yang sangat potensial.
* **Peluang Kredit Korporat:** Sektor industri yang tumbuh subur dengan capex besar (seperti Logam Dasar dan Transportasi) merupakan target utama untuk *Corporate Lending*, *Trade Finance*, dan *Cash Management*.
* **Mitigasi Risiko:** Sektor yang stagnan atau daerah dengan penyerapan tenaga kerja rendah memberikan sinyal risiko gagal bayar (*Non-Performing Loan*) yang lebih tinggi bagi debitur terkait.

---

## ⚙️ Struktur Proyek

Proyek ini telah dikonfigurasi secara rapi dan profesional dengan struktur sebagai berikut:

```text
Data Realisasi Investasi/
├── .gitignore                                      # Konfigurasi ignore file agar git tetap bersih
├── README.md                                       # Dokumentasi utama (file ini)
├── Analisis_Investasi_Q1_2025.ipynb                # Interactive notebook untuk simulasi cabang (Q1)
├── analisis_tahunan.py                             # Script python otomatis untuk analisis full-year 2025
├── Data Realisasi Investasi Triwulan I Tahun 2025.csv   # Data mentah Q1
├── Data Realisasi Investasi Triwulan II Tahun 2025.csv  # Data mentah Q2
├── Data Realisasi Investasi Triwulan III Tahun 2025.csv # Data mentah Q3
├── Data Realisasi Investasi Triwulan IV Tahun 2025.csv  # Data mentah Q4
└── outputs/                                        # Visualisasi premium yang dihasilkan otomatis
    ├── 01_tren_investasi_tki_2025.png              # Tren Triwulanan (Investasi vs TKI)
    ├── 02_top_10_provinsi_2025.png                 # Peta prioritas provinsi BNI
    ├── 03_top_10_sektor_2025.png                   # Sektor target utama penyaluran kredit
    └── 04_distribusi_jawa_luar_jawa_2025.png       # Perbandingan distribusi Jawa vs Luar Jawa
```

---

## 📊 Struktur Data (CSV)

Setiap dataset kuartal memiliki skema kolom yang konsisten sebanyak **14 kolom**, yang memungkinkan penggabungan secara langsung tanpa kendala:

| No | Nama Kolom | Tipe Data | Deskripsi |
|---|---|---|---|
| 1 | `periode` | String / Object | Kuartal realisasi investasi dilakukan (misal: "Triwulan I 2025") |
| 2 | `status_penanaman_modal` | String | PMA (Penanaman Modal Asing) atau PMDN (Dalam Negeri) |
| 3 | `regional` | String | Asal negara atau regional investor |
| 4 | `negara` | String | Negara spesifik investor asing (atau Indonesia jika PMDN) |
| 5 | `sektor_utama` | String | Klasifikasi sektor utama (Primer, Sekunder, Tersier) |
| 6 | `nama_sektor` | String | Nama bidang industri spesifik |
| 7 | `deskripsi_kbli_2digit` | String | Deskripsi KBLI standar pemerintah Indonesia |
| 8 | `provinsi` | String | Provinsi lokasi realisasi investasi |
| 9 | `kabupaten_kota` | String | Kabupaten/Kota lokasi spesifik investasi |
| 10 | `jawa_luar_jawa` | String | Kategori wilayah ("Jawa" atau "Luar Jawa") |
| 11 | `pulau` | String | Nama pulau lokasi investasi |
| 12 | `investasi_rp_juta` | Float / Numeric | Nilai investasi dalam jutaan Rupiah |
| 13 | `investasi_us_ribu` | Float / Numeric | Nilai investasi dalam ribuan USD |
| 14 | `tki` | Float / Numeric | Jumlah penyerapan Tenaga Kerja Indonesia (orang) |

---

## 📈 Hasil Analisis Strategis Tahunan 2025

Berdasarkan pengolahan data otomatis yang dilakukan oleh `analisis_tahunan.py` terhadap seluruh kuartal di tahun 2025, diperoleh temuan intelijen bisnis sebagai berikut:

### 1. Ringkasan Utama 2025
* **Total Realisasi Investasi:** **Rp 1,931.17 Triliun** (atau setara **USD 119.89 Miliar**)
* **Total Penyerapan Tenaga Kerja (TKI):** **2,710,532 orang** teresap ke sektor formal
* **Total Proyek Aktif:** **126,082 proyek** investasi terdaftar

### 2. Tren Realisasi per Kuartal
Realisasi investasi di Indonesia menunjukkan pertumbuhan yang konsisten dan stabil sepanjang tahun 2025:

| Kuartal | Nilai Investasi (Rp Triliun) | Nilai Investasi (USD Juta) | Penyerapan TKI (Orang) | Jumlah Proyek |
| :---: | :---: | :---: | :---: | :---: |
| **Q1** | Rp 465.21 T | USD 29,075.72 | 594,104 | 29,825 |
| **Q2** | Rp 477.66 T | USD 29,043.84 | 665,764 | 35,003 |
| **Q3** | Rp 491.42 T | USD 30,713.46 | 696,478 | 31,241 |
| ****Q4** | Rp 496.88 T | USD 31,054.98 | 754,186 | 30,013 |
| **TOTAL** | **Rp 1,931.17 T** | **USD 119,888.00** | **2,710,532** | **126,082** |

> [!NOTE]
> Terjadi akselerasi penyerapan tenaga kerja yang signifikan pada kuartal IV (Q4) mencapai **754 ribu TKI**, menjadikannya periode emas bagi ekspansi produk retail perbankan seperti *Payroll* dan *Consumer Loans*.

### 3. Top 5 Provinsi Prioritas BNI
Provinsi dengan realisasi investasi tertinggi merupakan sasaran utama untuk alokasi dana dan penempatan tim RM spesialis korporat:
1. **Jawa Barat:** Rp 296.83 Triliun (Pusat manufaktur & otomotif nasional)
2. **DKI Jakarta:** Rp 270.93 Triliun (Pusat kantor pusat korporasi & sektor jasa)
3. **Jawa Timur:** Rp 145.11 Triliun (Hub industri makanan-minuman & perdagangan timur)
4. **Banten:** Rp 130.16 Triliun (Hub industri kimia & logistik barat Jawa)
5. **Sulawesi Tengah:** Rp 127.18 Triliun (Pusat hilirisasi mineral & smelter nikel global)

### 4. Top 5 Sektor Terpanas (Target Kredit)
Sektor-sektor ini terbukti memiliki perputaran modal paling aktif di Indonesia sepanjang tahun 2025:
1. **Industri Logam Dasar & Barang Logam:** **Rp 262.04 Triliun** (Hilirisasi nikel/tembaga - peluang Kredit Investasi besar)
2. **Transportasi, Gudang, & Telekomunikasi:** **Rp 211.01 Triliun** (Infrastruktur konektivitas - peluang Sindikasi & Cash Management)
3. **Pertambangan:** **Rp 199.65 Triliun** (Peluang *Trade Finance*, *LC*, & Ekspor-Impor)
4. **Jasa Lainnya:** **Rp 170.51 Triliun** (Peluang solusi perbankan digital & *Treasury*)
5. **Perumahan, Kawasan Industri, & Perkantoran:** **Rp 140.39 Triliun** (Peluang Kredit Konstruksi & KPR massal)

### 5. Keseimbangan Kewilayahan (Jawa vs Luar Jawa)
Distribusi investasi tahun 2025 menunjukkan hasil yang sangat positif bagi program pemerataan ekonomi nasional:
* **Luar Jawa:** **Rp 991.20 Triliun (51.3%)**
* **Jawa:** **Rp 939.97 Triliun (48.7%)**

> [!TIP]
> Fakta bahwa investasi di Luar Jawa sedikit mendominasi (51.3%) menunjukkan pentingnya BNI untuk tidak hanya berfokus pada pulau Jawa, melainkan memperkuat cabang-cabang strategis di luar Jawa (terutama Sulawesi Tengah, Kalimantan Timur, dan Sumatra Selatan) yang kaya akan hilirisasi komoditas dan pertambangan.

---

## 💻 Instalasi & Panduan Menjalankan

### Persyaratan Sistem
Pastikan Python 3.8 ke atas sudah terpasang di komputer Anda.

### 1. Kloning & Masuk ke Direktori
Jika repositori sudah di-push ke GitHub, Anda dapat mengkloningnya, atau langsung membuka terminal di dalam folder lokal saat ini.

### 2. Install Dependensi
Pasang pustaka visualisasi dan analisis data melalui pip:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 3. Jalankan Analisis Otomatis (Full-Year 2025)
Jalankan script Python untuk memperbarui ringkasan statistik dan memperbarui grafik visualisasi premium di folder `outputs/`:
```bash
python3 analisis_tahunan.py
```

### 4. Jalankan Jupyter Notebook (Simulasi Interaktif)
Untuk RM yang ingin menganalisis wilayah cakupan kantor cabangnya secara spesifik (misal: mencari sektor terkuat di Bekasi atau Makassar), Anda dapat menjalankan notebook interaktif:
```bash
jupyter notebook Analisis_Investasi_Q1_2025.ipynb
```
*Gunakan fungsi interaktif `analyze_branch_area('Nama Kota')` di cell akhir notebook untuk melakukan simulasi cepat.*

---

## 🚀 Panduan Push ke GitHub

Sebelum melakukan push ke GitHub, ikuti panduan langkah demi langkah berikut agar repositori Anda terlihat sangat profesional dan bersih:

### Langkah 1: Inisialisasi Repositori Git Lokal
Buka Terminal/Git Bash di folder proyek ini, lalu jalankan:
```bash
git init
```

### Langkah 2: Daftarkan Perubahan dengan Memanfaatkan `.gitignore`
Proyek ini sudah dilengkapi dengan berkas `.gitignore` yang akan secara otomatis menyaring file sampah macOS (`.DS_Store`), cache Python (`__pycache__`), dan checkpoint Jupyter (`.ipynb_checkpoints`).
```bash
git add .
```

### Langkah 3: Lakukan Commit Pertama Anda
Buat pesan commit yang deskriptif dan profesional:
```bash
git commit -m "feat: inisialisasi project analisis realisasi investasi BNI 2025 dengan visualisasi tahunan"
```

### Langkah 4: Hubungkan ke GitHub & Push
Buat sebuah repositori baru di akun GitHub Anda (misal dinamakan `bni-investasi-analysis-2025`), lalu hubungkan dengan perintah berikut:
```bash
# Ganti URL di bawah dengan URL repositori Anda
git remote add origin https://github.com/username/bni-investasi-analysis-2025.git
git branch -M main
git push -u origin main
```

---

*Dikembangkan dengan penuh dedikasi oleh tim **Antigravity AI Assistant** untuk kesuksesan ekspansi portofolio bisnis Bank BNI.*
