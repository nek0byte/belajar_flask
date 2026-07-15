# 10 -- Selanjutnya: Apa Lagi yang Perlu Dipelajari

## Tujuan Pembelajaran

- Apa yang sudah kamu pelajari sejauh ini (review)
- Topik apa yang perlu dipelajari selanjutnya
- Proyek-proyek untuk latihan mandiri


## Review: Yang Sudah Kamu Pelajari

Selamat! Kamu sudah menyelesaikan materi dasar backend dengan Flask.
Mari kita review apa saja yang sudah kamu kuasai:

### Level 1: Konsep Web

| Materi | Yang Kamu Kuasai |
|---|---|
| 00 | Paham beda frontend dan backend, client dan server |
| 01 | Paham URL, HTTP, request-response, GET vs POST |

### Level 2: Praktik Flask

| Materi | Yang Kamu Kuasai |
|---|---|
| 02 | Membuat virtual environment, install Flask |
| 03 | Membuat aplikasi Flask, route, `@app.route()`, `app.run()` |
| 04 | Memisahkan HTML ke template, `render_template()`, Jinja2 |
| 05 | Menambahkan CSS, `url_for('static', ...)` |

### Level 3: CRUD Database

| Materi | Yang Kamu Kuasai |
|---|---|
| 06 | Form HTML, method POST, `request.form`, flash, redirect |
| 07 | Database SQLite, model, `db.session.add()`, `commit()` |
| 08 | Edit dan hapus data, parameter URL (`<int:id>`) |

### Level 4: Struktur

| Materi | Yang Kamu Kuasai |
|---|---|
| 09 | Blueprint, memisahkan kode ke beberapa file |

Kamu sekarang bisa membuat aplikasi web sederhana dengan Python dan Flask!


## Topik Selanjutnya

Setelah menguasai dasar, berikut topik-topik yang perlu dipelajari untuk
menjadi backend developer yang lebih baik:

### 1. Error Handling

Sekarang, jika pengguna mengakses halaman yang tidak ada, Flask menampilkan
halaman error bawaan. Kamu bisa membuat halaman error kustom.

```python
@bp.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
```

Pelajari juga: `@app.errorhandler(500)` untuk error server.

### 2. Konfigurasi dengan .env

Sekarang `SECRET_KEY` dan `DATABASE_URL` ditulis langsung di kode. Ini
tidak aman untuk production. Pelajari cara menyimpan konfigurasi di file
`.env` menggunakan `python-dotenv`.

```python
# .env
SECRET_KEY=rahasia-super-aman
DATABASE_URL=sqlite:///board.db
```

### 3. Logging

Logging adalah cara mencatat apa yang terjadi di aplikasi ke file.
Berguna untuk melacak error.

```python
app.logger.info('Pengguna mengakses halaman utama')
app.logger.error(f'Error: {str(error)}')
```

### 4. Testing (Pengujian)

Testing adalah cara memastikan aplikasi berfungsi dengan benar secara
otomatis. Gunakan `pytest`.

```python
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
```

### 5. REST API

Selain halaman HTML, backend juga bisa menyediakan data dalam format JSON
untuk aplikasi lain (mobile app, frontend JavaScript).

```
GET /api/messages  -->  [{ "id": 1, "title": "Halo" }, ...]
```

### 6. Autentikasi (Login)

Hampir semua aplikasi butuh login. Pelajari:
- Session Flask (`session['user_id'] = ...`)
- Hash password (`generate_password_hash`)
- Decorator `@login_required`

### 7. Deployment (Menerbitkan)

Setelah aplikasi selesai, kamu perlu "menaikkan" ke internet agar orang
lain bisa mengakses. Pelajari:

| Tool | Fungsi |
|---|---|
| Gunicorn | Server production (ganti `app.run()`) |
| Nginx | Reverse proxy, handle HTTPS, serve static files |
| PythonAnywhere | Hosting gratis untuk Flask |
| Render / Railway | Hosting modern dengan git integration |


## Rekomendasi Belajar

### Urutan Belajar Topik Lanjutan

```
1. Error handling      (buat halaman 404 kustom)
2. Konfigurasi .env    (pisahkan rahasia dari kode)
3. Logging             (catat error ke file)
4. Testing             (pytest untuk Flask)
5. REST API            (JSON, jsonify)
6. Autentikasi         (login, session)
7. Deployment          (PythonAnywhere / Render)
```

### Sumber Belajar

| Sumber | Link |
|---|---|
| Dokumentasi Flask | https://flask.palletsprojects.com/ |
| Flask Mega Tutorial | https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial |
| PythonAnywhere | https://www.pythonanywhere.com/ |

### Tips Belajar

1.  **Buat proyek sendiri** -- jangan hanya ikut tutorial. Buat aplikasi
    yang kamu butuhkan sendiri.
2.  **Baca error** -- error bukan musuh. Error memberitahu apa yang salah.
    Bacalah perlahan.
3.  **Googling** -- "cara membuat login Flask" akan memberikan banyak
    hasil. Biasakan mencari solusi sendiri.
4.  **Tiru, lalu modifikasi** -- ambil kode orang lain, pahami, lalu ubah.


## Proyek Latihan

Coba buat salah satu proyek ini untuk mempraktikkan semua yang sudah
dipelajari:

| Proyek | Fitur yang Dipelajari |
|---|---|
| **To-Do List** | CRUD, checklist selesai/belum, filter |
| **Buku Catatan** | CRUD, kategori, pencarian |
| **Buku Tamu Digital** | CRUD, tanggal, sorting |
| **Katalog Produk** | CRUD dengan gambar, kategori |
| **Blog Mini** | Post, komentar, user |

Setiap proyek di atas bisa dibuat dengan Flask, database SQLite, dan
pengetahuan yang sudah kamu pelajari.


## Kata Penutup

Kamu sudah menyelesaikan 10 materi dasar Flask. Dari tidak tahu apa itu
backend, sekarang bisa membuat aplikasi web dengan database sendiri.

**Yang terpenting**: teruslah praktik. Semakin sering membuat proyek,
semakin paham konsepnya. Jangan takut error -- setiap error adalah
pelajaran.

Selamat belajar dan semoga berhasil!
