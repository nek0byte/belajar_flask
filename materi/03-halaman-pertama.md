# 03 -- Halaman Pertama dengan Flask

## Tujuan Pembelajaran

- Membuat aplikasi Flask minimal
- Memahami apa itu route dan URL
- Membuat halaman web pertama dengan Flask
- Menjalankan server Flask di komputermu

Ini adalah **materi paling penting**. Pahami baik-baik.


## Cerita Dulu: Papan Petunjuk Arah

Bayangkan kamu bekerja di resepsionis sebuah gedung besar. Di gedung itu ada
banyak ruangan: Ruang A, Ruang B, Ruang C.

Tugasmu adalah: ketika seseorang datang dan bertanya "Ruang A di mana?",
kamu menunjuk ke arah yang benar. Kamu adalah **router**.

Dalam Flask, konsep ini disebut **routing**:
- Seseorang datang ke URL `/beranda` --> kamu tunjukkan halaman beranda
- Seseorang datang ke URL `/tentang` --> kamu tunjukkan halaman tentang

Flask adalah **resepsionis** yang mengarahkan tamu ke halaman yang tepat.


## Membuat Aplikasi Flask Minimal

Buat file baru bernama `app.py` di dalam folder `learn_flask` yang sudah
kita buat sebelumnya. Ketik kode berikut:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Halo, Dunia!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
```

### Penjelasan Baris Per Baris

**Baris 1: `from flask import Flask`**

Kita mengambil class `Flask` dari library flask. Class adalah cetakan
untuk membuat objek. `Flask` adalah cetakan untuk membuat aplikasi web.

**Baris 3: `app = Flask(__name__)`**

Kita membuat **objek aplikasi** bernama `app`. Objek ini adalah jantung
dari aplikasi Flask kita. Parameter `__name__` memberi tahu Flask di mana
lokasi file ini, agar Flask bisa menemukan folder `templates/` dan
`static/` nantinya.

`__name__` adalah variabel khusus Python yang berisi `'__main__'` jika
file ini dijalankan langsung.

**Baris 5: `@app.route('/')`**

Ini adalah **decorator**. Kamu sudah belajar decorator di Python OOP kan?
Decorator ini "membungkus" fungsi di bawahnya dan menambahkan perilaku.

Terjemahan: "Flask, tolong daftarkan URL `/` (halaman utama) ke fungsi
`home()` di bawah ini."

Jadi ketika seseorang membuka URL `http://localhost:8000/`, Flask akan
memanggil fungsi `home()`.

**Baris 6-7: `def home():`** dan **`return '<h1>Halo, Dunia!</h1>'`**

Fungsi `home()` adalah fungsi biasa Python. Bedanya, dia mengembalikan
sebuah string HTML. String ini akan dikirim oleh Flask ke browser
sebagai response.

**Baris 9: `if __name__ == '__main__':`**

Ini adalah Python standar. Artinya: "Jika file ini dijalankan langsung
(bukan di-import), jalankan kode di bawahnya."

**Baris 10: `app.run(host='0.0.0.0', port=8000, debug=True)`**

Ini memerintahkan Flask untuk menjalankan server development.

| Parameter | Arti |
|---|---|
| `host='0.0.0.0'` | Bisa diakses dari komputer lain di jaringan yang sama |
| `port=8000` | Gunakan port 8000 (bisa diganti 5000, 8080, dll) |
| `debug=True` | Auto-reload saat ada perubahan kode + tampilkan error detail |


## Menjalankan Aplikasi

### Langkah 1: Aktifkan venv

```bash
cd learn_flask
source venv/bin/activate    # Linux/Mac
# atau venv\Scripts\activate  # Windows
```

### Langkah 2: Jalankan app.py

```bash
python app.py
```

Kamu akan melihat output seperti ini:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
```

### Langkah 3: Buka di browser

Buka browser dan ketik: `http://localhost:8000`

Kamu akan melihat tulisan "Halo, Dunia!" di halaman browser.

Selamat! Kamu baru saja membuat website pertamamu dengan Flask.

> **Mengapa ada 2 alamat?**
> `http://127.0.0.1:8000` dan `http://localhost:8000` adalah sama.
> `127.0.0.1` adalah alamat "rumah sendiri" (localhost).


## Eksperimen: Menambah Route Baru

Coba tambahkan route baru di file `app.py`. Tambahkan kode **setelah**
fungsi `home()` dan **sebelum** `if __name__`:

```python
@app.route('/tentang')
def tentang():
    return '<h1>Tentang Kami</h1><p>Ini halaman tentang.</p>'
```

Karena `debug=True`, kamu tidak perlu restart server. Cukup simpan file,
buka `http://localhost:8000/tentang` di browser.

### Latihan: Route dengan Nama

Kamu bisa membuat route yang menerima parameter:

```python
@app.route('/sapa/<nama>')
def sapa(nama):
    return f'<h1>Halo, {nama}!</h1>'
```

Coba akses `http://localhost:8000/sapa/Budi`. Maka `nama` akan berisi
string `'Budi'`. Coba ganti `Budi` dengan namamu sendiri.


## Ringkasan

| Konsep | Kode | Arti |
|---|---|---|
| Buat aplikasi | `app = Flask(__name__)` | Buat objek aplikasi Flask |
| Daftar route | `@app.route('/')` | Hubungkan URL dengan fungsi |
| Fungsi view | `def home():` | Fungsi yang dipanggil saat URL diakses |
| Return HTML | `return '<h1>Halo</h1>'` | Kirim HTML sebagai response |
| Parameter URL | `@app.route('/<nama>')` | Tangkap bagian dinamis dari URL |
| Jalankan server | `app.run(debug=True)` | Mulai server development |

**Yang penting dipahami:**
Ketika browser membuka URL, Flask mencocokkan URL dengan daftar route
yang sudah didaftarkan (`@app.route`). Jika cocok, fungsi yang sesuai
dipanggil. Hasil fungsi dikirim balik ke browser.
