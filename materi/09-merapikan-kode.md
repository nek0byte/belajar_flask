# 09 -- Merapikan Kode: Blueprint dan Struktur Proyek

## Tujuan Pembelajaran

- Memahami kenapa kode perlu dipecah ke beberapa file
- Menggunakan Blueprint untuk mengelompokkan route
- Mengenal struktur proyek Flask yang rapi


## Analogi: Lemari Arsip vs Tumpukan Kertas

Bayangkan semua catatanmu ditulis di satu lembar kertas raksasa. Catatan
belanja, jadwal kuliah, nomor telepon, ide proyek -- semuanya di satu
kertas. Kacau, kan?

Lebih baik: setiap kategori punya **folder sendiri**. Belanja di folder
`belanja`, kuliah di folder `kuliah`.

Sama dengan kode program. Semakin besar aplikasi, semakin penting untuk
memisah-misah kode ke file yang berbeda.

### Masalah Satu File Besar

Selama ini semua route ditulis di satu file `routes.py`. Ini ok untuk
10 route. Tapi bagaimana jika aplikasi punya:

- 30 route untuk halaman umum
- 20 route untuk admin
- 15 route untuk API
- 10 route untuk autentikasi

Semua di satu file? Akan sulit:
- Mencari route tertentu
- Dua programmer mengedit file yang sama (conflict Git)
- Memahami struktur aplikasi

### Solusi: Blueprint

Blueprint adalah cara Flask mengelompokkan route berdasarkan **fitur**.
Misal:

```
board/routes.py      --> route untuk fitur "board" (halaman umum)
board/auth.py        --> route untuk fitur "auth" (login, register)
board/api.py         --> route untuk fitur "api" (endpoint JSON)

Masing-masing adalah BLUEPRINT terpisah.
```


## Blueprint: Cara Kerja

Blueprint mirip dengan `app.route()` yang biasa kamu pakai, tapi
`app` diganti `bp`.

### Sebelum (tanpa Blueprint -- yang ada di proyek)

Di `board/routes.py`:

```python
from flask import Blueprint, render_template, ...

bp = Blueprint('board', __name__)

@bp.route('/')
def home(): ...

@bp.route('/create', methods=['GET', 'POST'])
def create(): ...
```

Di `board/__init__.py`:

```python
from . import routes
app.register_blueprint(routes.bp)
```

Kenapa sudah pakai Blueprint? Agar nanti bisa menambah blueprint lain
tanpa mengubah file `routes.py`.

### Menambah Blueprint Kedua

Buat file `board/auth.py`:

```python
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login')
def login():
    return '<h1>Halaman Login</h1>'


@auth_bp.route('/register')
def register():
    return '<h1>Halaman Register</h1>'
```

Perhatikan `url_prefix='/auth'`. Artinya semua route di blueprint ini
akan diawali `/auth`:

- `/auth/login`
- `/auth/register`

Daftarkan di `board/__init__.py`:

```python
from . import routes
from . import auth
app.register_blueprint(routes.bp)
app.register_blueprint(auth.auth_bp)
```

### url_prefix

`url_prefix` adalah awalan URL untuk semua route dalam blueprint.

| Blueprint | url_prefix | Route | URL Final |
|---|---|---|---|
| `board` | (tidak ada) | `/` | `/` |
| `board` | (tidak ada) | `/create` | `/create` |
| `auth` | `/auth` | `/login` | `/auth/login` |
| `auth` | `/auth` | `/register` | `/auth/register` |
| `admin` | `/admin` | `/dashboard` | `/admin/dashboard` |


## url_for dengan Blueprint

Kamu sudah pakai `url_for('board.home')` di template. Formatnya:

```
url_for('nama_blueprint.nama_fungsi')
```

| url_for | Hasil URL |
|---|---|
| `url_for('board.home')` | `/` |
| `url_for('board.create')` | `/create` |
| `url_for('board.edit', id=5)` | `/edit/5` |
| `url_for('board.delete', id=3)` | `/delete/3` |

Jika ada blueprint `auth`:

| url_for | Hasil URL |
|---|---|
| `url_for('auth.login')` | `/auth/login` |
| `url_for('auth.register')` | `/auth/register` |


## Struktur Proyek Flask

Seiring proyekmu bertambah besar, struktur foldermu bisa berkembang.

### Kecil (seperti proyek ini)

```
learn_flask/
├── run.py
├── requirements.txt
└── board/
    ├── __init__.py       # App factory + konfigurasi
    ├── routes.py         # Semua route
    ├── models.py         # Model database
    ├── templates/
    └── static/
```

### Sedang

```
project/
├── run.py
├── config.py             # Konfigurasi terpisah
├── requirements.txt
└── myapp/
    ├── __init__.py       # App factory
    ├── models/
    │   ├── user.py
    │   └── post.py
    ├── blueprints/
    │   ├── main.py
    │   ├── auth.py
    │   └── api.py
    ├── templates/
    └── static/
```

### Besar

```
project/
├── run.py
├── config.py
├── requirements.txt
├── tests/                # File test terpisah
├── migrations/           # Database versioning
└── myapp/
    ├── __init__.py
    ├── models/
    ├── blueprints/
    ├── templates/
    ├── static/
    ├── utils/            # Fungsi bantuan
    └── services/         # Logika bisnis
```

Untuk sekarang, struktur proyek ini sudah cukup. Fokus dulu memahami
konsepnya, bukan ukuran foldernya.


## Ringkasan

| Konsep | Kode |
|---|---|
| Buat Blueprint | `bp = Blueprint('nama', __name__)` |
| Route di Blueprint | `@bp.route('/')` (bukan `@app.route`) |
| Daftarkan Blueprint | `app.register_blueprint(bp)` |
| Prefix URL | `Blueprint('nama', __name__, url_prefix='/auth')` |
| url_for | `url_for('nama_bp.nama_fungsi')` |
| Banyak Blueprint | Buat file terpisah untuk setiap fitur |

Yang penting: **Blueprint adalah alat untuk mengorganisir kode**. Ketika
aplikasimu mulai punya banyak fitur, pisahkan ke blueprint berbeda.
