# 08 -- Mengelola Data: Edit dan Hapus

## Tujuan Pembelajaran

- Membuat route untuk mengedit data yang sudah ada
- Membuat route untuk menghapus data
- Mengirim ID data melalui URL
- Menangani kasus data tidak ditemukan


## Cerita Dulu: Buku Tamu (Lanjutan)

Ingat buku tamu dari materi 06? Sekarang kita tambah fitur:

1. **Lihat** semua pesan -- sudah bisa
2. **Tambah** pesan baru -- sudah bisa
3. **Edit** pesan yang sudah ada -- akan dibuat
4. **Hapus** pesan -- akan dibuat

Ini disebut **CRUD**: Create, Read, Update, Delete. Empat operasi dasar
di aplikasi database manapun.


## Route Parameter: Tangkap ID dari URL

Untuk mengedit atau menghapus, kita harus tahu **pesan mana** yang mau
diedit. Caranya: kirim ID pesan melalui URL.

```
/edit/1    -> edit pesan dengan ID 1
/edit/2    -> edit pesan dengan ID 2
/delete/3  -> hapus pesan dengan ID 3
```

Di Flask, kita tangkap bagian URL yang berubah-ubah dengan `<int:id>`:

```python
@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # id berisi angka dari URL
    ...
```

| Bagian URL | Arti |
|---|---|
| `<int:id>` | Ambil angka dari URL, simpan ke variabel `id` |
| `def edit(id):` | Fungsi menerima parameter `id` |

Bisa juga pakai tipe lain:

| Tipe | Contoh URL | Nilai di Python |
|---|---|---|
| `<int:id>` | `/edit/5` | `id = 5` (angka) |
| `<string:nama>` | `/sapa/Budi` | `nama = 'Budi'` (teks) |
| `<path:sisa>` | `/files/folder/file.txt` | `sisa = 'folder/file.txt'` (path panjang) |

> **Kenapa pakai `<int:id>` bukan `<string:id>`?**
> Karena ID adalah angka. Flask akan otomatis mengubah string "5" jadi
> integer 5. Jika ada huruf (misal `/edit/abc`), Flask akan return 404.


## Route Edit: Mengubah Data yang Ada

### Alur Edit

```
1. Pengguna klik tombol "Edit" pada pesan tertentu
        │
        ▼
2. Browser buka /edit/<id> (method GET)
        │
        ▼
3. Ambil data pesan dari database berdasarkan id
        │
        ▼
4. Tampilkan form yang sudah terisi data lama
        │
        ▼
5. Pengguna ubah data, klik "Simpan"
        │
        ▼
6. Browser kirim POST ke /edit/<id>
        │
        ▼
7. Ambil data baru dari form
        │
        ▼
8. Update data di database
        │
        ▼
9. Redirect ke halaman utama
```

### Kode Route Edit

```python
@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Cari pesan di database
    msg = db.session.get(Message, id)

    # Jika tidak ditemukan
    if msg is None:
        flash('Pesan tidak ditemukan!', 'error')
        return redirect(url_for('board.home'))

    # Jika pengirim mengirim data (POST)
    if request.method == 'POST':
        msg.title = request.form['title']
        msg.author = request.form['author']
        msg.body = request.form['body']
        db.session.commit()
        flash('Pesan berhasil diubah!', 'success')
        return redirect(url_for('board.home'))

    # Jika GET, tampilkan form dengan data lama
    return render_template('edit.html', message=msg)
```

### Penjelasan

| Baris | Arti |
|---|---|
| `msg = db.session.get(Message, id)` | Cari pesan dengan ID tertentu dari database |
| `if msg is None:` | Jika tidak ada pesan dengan ID itu, tampilkan error dan redirect |
| `msg.title = request.form['title']` | Ubah atribut title dengan data dari form |
| `db.session.commit()` | Simpan perubahan ke database |
| `render_template('edit.html', message=msg)` | Kirim data pesan ke template untuk diisi di form |

### Form Edit

File `board/templates/edit.html`:

```html
{% extends 'base.html' %}

{% block title %}Edit Pesan{% endblock %}

{% block content %}
    <h1>Edit Pesan</h1>

    <form method="POST">
        <div>
            <label for="title">Judul</label>
            <input type="text" id="title" name="title"
                   value="{{ message.title }}" required>
        </div>
        <div>
            <label for="author">Nama</label>
            <input type="text" id="author" name="author"
                   value="{{ message.author }}" required>
        </div>
        <div>
            <label for="body">Isi Pesan</label>
            <textarea id="body" name="body" rows="5"
                      required>{{ message.body }}</textarea>
        </div>
        <button type="submit">Simpan</button>
        <a href="{{ url_for('board.home') }}">Batal</a>
    </form>
{% endblock %}
```

Perbedaan dengan form create:
- `value="{{ message.title }}"` -- form sudah terisi data lama
- `{{ message.body }}` di textarea -- isi textarea dengan data lama
- Tombol "Batal" kembali ke beranda tanpa menyimpan


## Route Delete: Menghapus Data

### Alur Hapus

```
1. Pengguna klik "Hapus" pada pesan
        │
        ▼
2. Konfirmasi: "Yakin ingin menghapus?"
        │
        ▼
3. Browser buka /delete/<id> (method GET)
        │
        ▼
4. Cari pesan di database
        │
        ▼
5. Hapus dari database
        │
        ▼
6. Redirect ke halaman utama
```

### Kode Route Delete

```python
@bp.route('/delete/<int:id>')
def delete(id):
    msg = db.session.get(Message, id)

    if msg is None:
        flash('Pesan tidak ditemukan!', 'error')
    else:
        db.session.delete(msg)
        db.session.commit()
        flash('Pesan berhasil dihapus!', 'success')

    return redirect(url_for('board.home'))
```

### Penjelasan

| Baris | Arti |
|---|---|
| `@bp.route('/delete/<int:id>')` | Route hanya untuk GET. Tidak perlu method POST karena hapus cukup sekali klik |
| `db.session.delete(msg)` | Hapus objek dari database (masih staging) |
| `db.session.commit()` | Simpan penghapusan ke database |

### Tombol Hapus (dengan Konfirmasi)

Di `index.html`:

```html
<a href="{{ url_for('board.delete', id=msg.id) }}"
   onclick="return confirm('Yakin ingin menghapus?')">Hapus</a>
```

`onclick="return confirm(...)"` adalah JavaScript. Browser akan menampilkan
pop-up konfirmasi. Jika klik "Batal", link tidak diikuti.


## Tombol Edit dan Hapus di Index

Update `index.html` untuk menampilkan tombol aksi:

```html
{% extends 'base.html' %}

{% block title %}Beranda - Message Board{% endblock %}

{% block content %}
    <h1>Message Board</h1>

    <a href="{{ url_for('board.create') }}" class="btn">+ Tambah Pesan</a>

    <div class="messages">
        {% for msg in messages %}
            <div class="message-card">
                <h3>{{ msg.title }}</h3>
                <p>{{ msg.body }}</p>
                <small>Oleh: {{ msg.author }}</small>
                <div class="actions">
                    <a href="{{ url_for('board.edit', id=msg.id) }}">Edit</a>
                    <a href="{{ url_for('board.delete', id=msg.id) }}"
                       onclick="return confirm('Yakin ingin menghapus?')">Hapus</a>
                </div>
            </div>
        {% else %}
            <p class="empty">Belum ada pesan. Jadilah yang pertama!</p>
        {% endfor %}
    </div>
{% endblock %}
```

Perhatikan `url_for('board.edit', id=msg.id)`:

| Bagian | Arti |
|---|---|
| `'board.edit'` | Nama blueprint + nama fungsi |
| `id=msg.id` | Nilai parameter `id` untuk route `/edit/<int:id>` |

Jadi jika `msg.id = 3`, URL yang dihasilkan: `/edit/3`.


## Eksperimen

1.  Coba akses `/edit/999` (ID yang tidak ada). Apa yang muncul?
2.  Hapus `if msg is None:` dari route edit. Akses ID yang tidak ada.
    Error apa yang muncul?
3.  Tambahkan kolom `email` ke model Message. Update form create dan edit
    untuk menyertakan email.
4.  Buat tombol "Batal" di form create yang kembali ke beranda.


## Ringkasan

| Konsep | Kode |
|---|---|
| Parameter URL | `@bp.route('/edit/<int:id>')` |
| Cari data by ID | `msg = db.session.get(Message, id)` |
| Cek data tidak ada | `if msg is None:` |
| Update data | Ubah atribut lalu `db.session.commit()` |
| Hapus data | `db.session.delete(msg)` lalu `db.session.commit()` |
| Link ke edit | `url_for('board.edit', id=msg.id)` |
| Link ke hapus | `url_for('board.delete', id=msg.id)` |
| Konfirmasi JS | `onclick="return confirm('Yakin?')"` |
