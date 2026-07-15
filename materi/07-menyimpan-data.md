# 07 -- Menyimpan Data ke Database

## Tujuan Pembelajaran

- Memahami apa itu database dan kenapa perlu
- Memahami apa itu ORM dengan analogi
- Membuat model database (tabel) menggunakan Python
- Menyimpan dan mengambil data dari database SQLite


## Cerita Dulu: Lemari Arsip

Di materi sebelumnya, kita menyimpan data pesan di **list** Python:

```python
messages = []
```

Ini seperti menaruh kertas di atas meja. Praktis untuk satu-dua kertas.
Tapi masalahnya:

1. **Hilang saat server mati** -- list hanya ada di RAM. Matikan server,
   data lenyap.
2. **Tidak bisa dicari** -- mau cari pesan dari "Budi" harus loop manual.
3. **Tidak bisa diakses banyak orang** -- list cuma untuk satu proses.

Solusinya: **Database**. Database adalah **lemari arsip** yang:
- Data tetap ada walau server mati (tersimpan di hard disk/file)
- Bisa mencari dengan cepat
- Bisa diakses banyak orang bersamaan

SQLite adalah database yang paling sederhana: satu file `.db` berisi
semua data. Cocok untuk belajar dan aplikasi kecil.


## Apa Itu ORM?

ORM = Object-Relational Mapping.

Di database, data disimpan dalam bentuk **tabel** (seperti Excel):

| id | title | author | body |
|---|---|---|---|
| 1 | Halo | Budi | Halo dunia |
| 2 | Test | Ani | Test 123 |

Di Python OOP, kita suka bekerja dengan **object**:

```python
pesan = Message(title='Halo', author='Budi', body='Halo dunia')
print(pesan.title)   # 'Halo'
```

**ORM adalah jembatan** antara tabel database dan object Python.
Dia memungkinkan kita menulis kode Python (`pesan.title`) tanpa harus
menulis SQL (`SELECT title FROM messages`).

Kita akan pakai **Flask-SQLAlchemy**, yang merupakan ORM untuk Flask.


## Membuat Model

Model adalah **class Python yang mewakili tabel di database**.

Buat file baru `board/models.py`:

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

# Buat objek database (masih kosong, belum terhubung ke app)
db = SQLAlchemy()


# Model = class yang mewakili tabel messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
```

### Penjelasan Setiap Kolom

| Baris Kode | Arti |
|---|---|
| `id = db.Column(db.Integer, primary_key=True)` | Kolom ID, angka, unik untuk setiap baris. Otomatis naik (1, 2, 3...) |
| `title = db.Column(db.String(100), nullable=False)` | Kolom judul, teks maks 100 karakter, wajib diisi |
| `author = db.Column(db.String(50), nullable=False)` | Kolom penulis, teks maks 50 karakter, wajib diisi |
| `body = db.Column(db.Text, nullable=False)` | Kolom isi pesan, teks panjang, wajib diisi |
| `created_at = db.Column(db.DateTime, default=...)` | Kolom tanggal, otomatis diisi waktu sekarang |

Tipe data kolom yang umum:

| Tipe | Untuk |
|---|---|
| `db.Integer` | Angka bulat |
| `db.String(100)` | Teks pendek (max 100 karakter) |
| `db.Text` | Teks panjang (tanpa batas) |
| `db.DateTime` | Tanggal dan jam |
| `db.Boolean` | True/False |
| `db.Float` | Angka desimal |

Parameter kolom:

| Parameter | Arti |
|---|---|
| `primary_key=True` | Kolom ini unik sebagai penanda setiap baris |
| `nullable=False` | Wajib diisi (tidak boleh kosong) |
| `default=...` | Nilai otomatis jika tidak diisi |
| `unique=True` | Tidak boleh ada nilai yang sama |


## Menghubungkan Database ke Aplikasi

Update `board/__init__.py`:

```python
from flask import Flask
from .models import db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rahasia123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///board.db'

    db.init_app(app)

    # Buat semua tabel yang belum ada
    with app.app_context():
        db.create_all()

    from . import routes
    app.register_blueprint(routes.bp)

    return app
```

### Penjelasan

| Baris Kode | Arti |
|---|---|
| `SQLALCHEMY_DATABASE_URI` | URL ke database. `sqlite:///board.db` artinya pakai SQLite, file bernama `board.db` |
| `db.init_app(app)` | Hubungkan database ke aplikasi Flask |
| `db.create_all()` | Buat tabel-tabel dari semua model yang ada (tidak dijalankan ulang jika tabel sudah ada) |
| `with app.app_context():` | Flask butuh "konteks aplikasi" untuk berinteraksi dengan database |


## Operasi Database Dasar (CRUD)

### CREATE -- Menyimpan Data Baru

```python
from .models import db, Message

# Buat object Python biasa
msg = Message(
    title='Halo Dunia',
    author='Budi',
    body='Ini pesan pertamaku!',
)

# Tambahkan ke session (staging)
db.session.add(msg)

# Simpan ke database (commit)
db.session.commit()
```

**Penting**: `db.session.add()` hanya staging. Data benar-benar tersimpan
setelah `db.session.commit()`.

### READ -- Mengambil Data

```python
# Ambil SEMUA pesan, diurutkan dari terbaru
messages = Message.query.order_by(Message.created_at.desc()).all()

# Ambil SATU pesan berdasarkan ID
msg = db.session.get(Message, 1)   # ambil pesan dengan id=1

# Ambil pesan dengan filter
pesan_budi = Message.query.filter_by(author='Budi').all()

# Ambil pesan pertama yang cocok
pesan_pertama = Message.query.first()

# Hitung jumlah pesan
jumlah = Message.query.count()
```

### UPDATE -- Mengubah Data

```python
# Ambil pesan yang mau diubah
msg = db.session.get(Message, 1)

# Ubah atributnya
msg.title = 'Judul Baru'
msg.body = 'Isi baru'

# Simpan perubahan
db.session.commit()
```

### DELETE -- Menghapus Data

```python
# Ambil pesan yang mau dihapus
msg = db.session.get(Message, 1)

# Hapus
db.session.delete(msg)

# Simpan
db.session.commit()
```


## Update Routes dengan Database

Sekarang kita ganti penyimpanan dari list ke database.

### Tampilkan Semua Pesan

```python
@bp.route('/')
def home():
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return render_template('index.html', messages=messages)
```

### Simpan Pesan Baru

```python
@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        msg = Message(
            title=request.form['title'],
            author=request.form['author'],
            body=request.form['body'],
        )
        db.session.add(msg)
        db.session.commit()
        flash('Pesan berhasil ditambahkan!', 'success')
        return redirect(url_for('board.home'))
    return render_template('create.html')
```

### Update Template untuk Object

Di materi 06, kita pakai `msg['title']` (dictionary). Sekarang `msg` adalah
object, jadi pakai `msg.title` (atribut).

Di `index.html`:

```html
<h3>{{ msg.title }}</h3>
<p>{{ msg.body }}</p>
<small>Oleh: {{ msg.author }} pada {{ msg.created_at.strftime('%d/%m/%Y %H:%M') }}</small>
```

> **`.strftime('%d/%m/%Y %H:%M')`** adalah fungsi Python untuk memformat
> tanggal. `%d` = tanggal, `%m` = bulan, `%Y` = tahun, `%H` = jam,
> `%M` = menit.


## Satu Penting: Session Database

`db.session` dalam SQLAlchemy berbeda dengan `session` Flask untuk login.

| Istilah | Arti di Sini |
|---|---|
| `db.session` | Koneksi ke database (staging area) |
| `add()` | Masukkan data ke staging |
| `commit()` | Simpan staging ke database |
| `rollback()` | Batalkan staging (jika error) |

Pola yang selalu diingat:

```python
# 1. Buat data
obj = Model(field1=value1, field2=value2)

# 2. Stage
db.session.add(obj)

# 3. Simpan (HARUS)
db.session.commit()
```

Tanpa `commit()`, data tidak akan tersimpan.


## Ringkasan

| Konsep | Penjelasan |
|---|---|
| Database | Tempat penyimpanan permanen (tidak hilang saat server mati) |
| SQLite | Database file-based, satu file `.db` |
| ORM | Jembatan antara tabel database dan object Python |
| Model | Class Python yang mewakili tabel |
| `db.session.add(obj)` | Stage objek untuk disimpan |
| `db.session.commit()` | Simpan perubahan ke database |
| `Model.query.all()` | Ambil semua data |
| `db.session.get(Model, id)` | Ambil satu data berdasarkan id |
| `.filter_by(field=value)` | Filter data |
| `.order_by(Model.field.desc())` | Urutkan |
