# 06 -- Menerima Input dari Pengguna

## Tujuan Pembelajaran

- Membuat form HTML yang mengirim data
- Membedakan GET dan POST di dalam kode
- Mengambil data dari form menggunakan `request.form`
- Memberi feedback ke pengguna dengan flash message
- Menerapkan PRG pattern (Post-Redirect-Get)


## Cerita Dulu: Buku Tamu

Bayangkan sebuah toko. Di pintu masuk ada **buku tamu**. Pengunjung bisa
menulis nama dan pesan. Pemilik toko bisa membaca semua pesan.

Ini adalah aplikasi pertama yang akan kita buat: **Message Board**
(papan pesan). Pengguna bisa:
1. Melihat semua pesan (GET /)
2. Menulis pesan baru (POST /create)


## GET vs POST (Review dari Materi 01)

| | GET | POST |
|---|---|---|
| Fungsi | Minta data | Kirim data |
| Data ada di | URL (query string) | Body (tidak terlihat) |
| Bisa di-bookmark | Ya | Tidak |
| Contoh | Buka halaman utama | Kirim form |

**Aturan penting backend:**
- **GET** hanya untuk membaca data. Jangan menghapus/mengubah data via GET.
- **POST** untuk mengirim data baru atau mengubah data.


## Route dengan Dua Method

Satu route bisa menerima lebih dari satu method. Misal:

```
URL /create:
  - Method GET  -> tampilkan form
  - Method POST -> proses data dari form
```

Di Flask, kita tulis:

```python
@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Ambil data dari form
        # Simpan ke database
        # Redirect ke halaman lain
        ...

    # Jika method GET, tampilkan form
    return render_template('create.html')
```


## Membuat Form HTML

File `board/templates/create.html`:

```html
{% extends 'base.html' %}

{% block title %}Tambah Pesan{% endblock %}

{% block content %}
    <h1>Tambah Pesan Baru</h1>

    <form method="POST">
        <div>
            <label for="title">Judul</label>
            <input type="text" id="title" name="title" required>
        </div>
        <div>
            <label for="author">Nama Kamu</label>
            <input type="text" id="author" name="author" required>
        </div>
        <div>
            <label for="body">Isi Pesan</label>
            <textarea id="body" name="body" rows="5" required></textarea>
        </div>
        <button type="submit">Kirim</button>
    </form>
{% endblock %}
```

### Penjelasan Form HTML

| Atribut | Arti |
|---|---|
| `<form method="POST">` | Form ini akan mengirim data via POST |
| `name="title"` | Nama field. Penting! Ini yang dipakai di `request.form['title']` |
| `required` | Browser tidak akan mengirim form jika field ini kosong |
| `type="submit"` | Tombol untuk mengirim form |

> **Nama `name`** di HTML harus **sama** dengan yang di `request.form['...']`.
> Jika di HTML `name="judul"`, di Python tulis `request.form['judul']`.

### Proses Form di Python

```python
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('board', __name__)

# Simpan data di list dulu (nanti diganti database)
messages = []


@bp.route('/')
def home():
    return render_template('index.html', messages=messages)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # 1. Ambil data dari form
        judul = request.form['title']
        penulis = request.form['author']
        isi = request.form['body']

        # 2. Simpan ke list (sementara)
        pesan_baru = {
            'title': judul,
            'author': penulis,
            'body': isi,
        }
        messages.append(pesan_baru)

        # 3. Beri tahu pengguna bahwa berhasil
        flash('Pesan berhasil ditambahkan!', 'success')

        # 4. Redirect ke halaman utama
        return redirect(url_for('board.home'))

    # Kalau GET, tampilkan form
    return render_template('create.html')
```


## Memahami Alurnya

```
Pengguna buka /create
        │
        ▼
Route /create (method GET)
        │
        ▼
Tampilkan form HTML
        │
        ▼
Pengguna isi form dan klik tombol Kirim
        │
        ▼
Browser kirim POST ke /create
        │
        ▼
Route /create (method POST)
        │
        ├── request.form['title']
        ├── request.form['author']
        └── request.form['body']
        │
        ▼
Simpan ke list --> flash('Berhasil!') --> redirect('/')
        │
        ▼
Browser diarahkan ke halaman utama
        │
        ▼
Halaman utama tampilkan daftar pesan (termasuk yang baru)
```


## Flash Message

`flash()` adalah cara Flask memberi pesan singkat ke pengguna.

```python
flash('Pesan berhasil ditambahkan!', 'success')
```

- Parameter 1: Isi pesan
- Parameter 2: Kategori (biasanya `'success'`, `'error'`, `'info'`)

Pesan flash disimpan di **session** (cuma sekali). Setelah ditampilkan,
dia hilang. Cocok untuk notifikasi "Berhasil!" atau "Gagal!".

### Menampilkan Flash Message

Di `base.html`:

```html
{% with msgs = get_flashed_messages(with_categories=true) %}
    {% if msgs %}
        {% for category, msg in msgs %}
            <div class="flash {{ category }}">{{ msg }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

Agar flash message berfungsi, kamu perlu `SECRET_KEY` di `__init__.py`:

```python
app.config['SECRET_KEY'] = 'kunci-rahasia-123'
```


## PRG Pattern: Post-Redirect-Get

Coba bayangkan apa yang terjadi jika **tidak pakai redirect**:

```python
# ❌ SALAH
if request.method == 'POST':
    messages.append(pesan_baru)
    return render_template('index.html', messages=messages)  # <-- langsung render
```

Pengguna melihat halaman utama. Tapi jika dia **refresh browser**, browser
akan mengirim POST lagi. Pesan yang sama tersimpan **dua kali**.

### Solusi: PRG (Post-Redirect-Get)

```python
# ✅ BENAR
if request.method == 'POST':
    messages.append(pesan_baru)
    flash('Berhasil!', 'success')
    return redirect(url_for('board.home'))  # <-- redirect
```

Alurnya:

```
POST /create --> simpan data --> redirect('/') --> browser GET /
```

Ketika pengguna refresh, browser hanya mengirim GET / (bukan POST lagi).
Pesan tidak akan tersimpan dua kali.


## Eksperimen

1.  Hapus `redirect()` dan langsung `render_template()` setelah POST.
    Refresh halaman. Apa yang terjadi?
2.  Ubah method form dari `POST` ke `GET`. Apa yang terjadi di URL?
3.  Tambahkan field `email` di form dan tangkap di Python.
4.  Ganti kategori flash dari `'success'` ke `'error'`. Apa yang berubah
    warnanya?


## Ringkasan

| Konsep | Kode |
|---|---|
| Route terima POST | `@bp.route('/url', methods=['GET', 'POST'])` |
| Cek method | `if request.method == 'POST':` |
| Ambil data form | `request.form['nama_field']` |
| Flash message | `flash('Pesan', 'category')` |
| Tampilkan flash | `get_flashed_messages(with_categories=true)` |
| Redirect | `redirect(url_for('nama_route'))` |
| PRG Pattern | POST -> redirect -> GET (cegah duplikasi data) |
