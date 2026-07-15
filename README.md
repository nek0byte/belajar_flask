# Belajar Flask -- Message Board App

Proyek ini adalah **mini project** untuk belajar backend development
dengan Flask dari nol. Cocok untuk pemula yang sudah belajar Python
dasar (sampai OOP) tapi belum tahu apa-apa tentang backend.

## Fitur Aplikasi

- Melihat semua pesan
- Membuat pesan baru
- Mengedit pesan
- Menghapus pesan
- Database SQLite (data tetap ada walau server mati)
- CSS styling
- Flash messages (notifikasi sukses/gagal)
- Struktur kode rapi dengan Blueprint

## Requirements

- Python 3.10 atau lebih baru
- Mengerti dasar Python: variabel, fungsi, list, dict, class, if/else, for loop

**Tidak perlu tahu apa pun tentang:**
- Web development
- HTML / CSS
- Database
- Server

Semua akan dijelaskan dari awal.

## Cara Menjalankan

```bash
# 1. Buka folder proyek
cd "nama folder proyek"

# 2. Buat virtual environment (hanya sekali)
python3 -m venv venv

# 3. Aktifkan virtual environment
source venv/bin/activate      # Linux / Mac
# venv\Scripts\activate       # Windows

# 4. Install Flask
pip install flask flask-sqlalchemy

# 5. Jalankan aplikasi
python run.py
```

Buka http://localhost:8000 di browser.

## Cara Belajar

<<<<<<< HEAD
=======

>>>>>>> 4990c5b413cd4ad0bbdd00986a34973b76d51114
### Fase 1: Pahami Konsep (baca, tidak perlu kode)

| # | File | Pelajari |
|---|---|---|
| 00 | `materi/00-apa-itu-backend.md` | Gambaran besar backend vs frontend, client vs server |
| 01 | `materi/01-cara-kerja-web.md` | Cara kerja web: URL, HTTP, request-response, GET vs POST |

### Fase 2: Praktik dengan Flask (baca + praktik + kode)

| # | File | Pelajari |
|---|---|---|
| 02 | `materi/02-persiapan-lingkungan.md` | Setup Python, venv, install Flask |
| 03 | `materi/03-halaman-pertama.md` | Aplikasi Flask pertama, routing |
| 04 | `materi/04-template-html.md` | Memisahkan HTML dari Python (Jinja2) |
| 05 | `materi/05-mempercantik-halaman.md` | CSS, file statis |
| 06 | `materi/06-input-dari-pengguna.md` | Form, POST, request, flash |
| 07 | `materi/07-menyimpan-data.md` | Database SQLite, model, simpan data |
| 08 | `materi/08-mengelola-data.md` | Edit dan hapus data (CRUD lengkap) |

### Fase 3: Struktur dan Selanjutnya

| # | File | Pelajari |
|---|---|---|
| 09 | `materi/09-merapikan-kode.md` | Blueprint, struktur proyek |
| 10 | `materi/10-selanjutnya.md` | Review, topik lanjutan, tips |

## Struktur Folder

```
learn_flask/
├── README.md                   # File ini -- panduan proyek
├── requirements.txt            # Daftar library yang dibutuhkan
├── run.py                      # File untuk menjalankan aplikasi
├── materi/                     # 10 file materi pembelajaran
│   ├── 00-apa-itu-backend.md
│   ├── 01-cara-kerja-web.md
│   ├── 02-persiapan-lingkungan.md
│   ├── 03-halaman-pertama.md
│   ├── 04-template-html.md
│   ├── 05-mempercantik-halaman.md
│   ├── 06-input-dari-pengguna.md
│   ├── 07-menyimpan-data.md
│   ├── 08-mengelola-data.md
│   ├── 09-merapikan-kode.md
│   └── 10-selanjutnya.md
└── board/                      # Package aplikasi Flask
    ├── __init__.py             # Inisialisasi aplikasi + konfigurasi
    ├── routes.py               # Semua route (URL) aplikasi
    ├── models.py               # Model database (tabel pesan)
    ├── templates/              # Template HTML
    │   ├── base.html           # Kerangka utama (layout)
    │   ├── index.html          # Halaman daftar pesan
    │   ├── create.html         # Form tambah pesan
    │   └── edit.html           # Form edit pesan
    └── static/                 # File statis (CSS, gambar)
        └── style.css           # Styling aplikasi
```

