# 04 -- Template HTML (Memisahkan Tampilan dari Logika)

## Tujuan Pembelajaran

- Memisahkan kode HTML dari kode Python
- Menggunakan `render_template` untuk memuat file HTML
- Mengirim variabel dari Python ke HTML
- Menggunakan template inheritance


## Cerita Dulu: Koki dan Desainer

Bayangkan sebuah restoran. Ada dua orang:
1. **Koki** (kita / Python) -- menyiapkan bahan dan memasak
2. **Desainer menu** (desainer HTML) -- mendesain tampilan menu

Di materi sebelumnya, koki **sekaligus** mendesain menu:

```python
return '<h1>Halo, Dunia!</h1>'
```

Ini seperti koki menulis sendiri tampilan menu. Praktis untuk satu
halaman. Tapi bagaimana jika ada 20 halaman? Atau ingin ganti font di
semua halaman? Ribet.

Solusinya: **Pisahkan!** Koki (Python) cukup siapkan data, serahkan
tampilan ke desainer (file HTML).


## render_template

Flask menyediakan fungsi `render_template` untuk memuat file HTML dan
menggabungkannya dengan data dari Python.

### Langkah 1: Buat Folder templates

Di dalam folder `board/`, buat folder bernama `templates/`:

```
learn_flask/
├── board/
│   ├── templates/        <-- buat folder ini
│   ├── __init__.py
│   └── routes.py
├── app.py (sementara)
└── venv/
```

> **Kenapa wajib bernama `templates/`?**
> Flask selalu mencari file HTML di folder `templates/`. Jika pakai nama
> lain, Flask tidak akan menemukan file HTML-nya.

### Langkah 2: Buat File HTML

Buat file `index.html` di dalam folder `templates/`:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Beranda</title>
</head>
<body>
    <h1>Halo, {{ nama }}!</h1>
    <p>Selamat datang di website pertamaku.</p>
</body>
</html>
```

Perhatikan `{{ nama }}`. Kurung kurawal dua ini adalah **sintaks Jinja2**
(baca: jin-ja). Artinya: "di sini akan diisi oleh variabel `nama` dari
Python."

### Langkah 3: Update Route

Ubah `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    nama = 'Budi'
    return render_template('index.html', nama=nama)


@app.route('/sapa/<nama>')
def sapa(nama):
    return render_template('index.html', nama=nama)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
```

### Penjelasan

| Kode | Arti |
|---|---|
| `from flask import render_template` | Ambil fungsi render_template dari Flask |
| `render_template('index.html', nama=nama)` | Cari file `index.html` di folder `templates/`, lalu isi variabel `nama` dengan nilai dari Python |

Parameter `nama=nama`:
- Yang kiri (`nama`) adalah **nama variabel di HTML** (yang ada di `{{ }}`)
- Yang kanan (`nama`) adalah **nilai dari Python**

Jadi `{{ nama }}` di HTML akan diganti menjadi `'Budi'`.

### Hasil

Buka `http://localhost:8000/sapa/Andi`. Browser akan menampilkan:

```
Halo, Andi!
Selamat datang di website pertamaku.
```


## Template Lebih Kompleks

Kita bisa mengirim data yang lebih rumit, seperti list atau dictionary.

### Di Python:

```python
@app.route('/daftar')
def daftar():
    teman = ['Budi', 'Ani', 'Caca', 'Dedi']
    return render_template('daftar.html', teman=teman)
```

### Di HTML (`templates/daftar.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daftar Teman</title>
</head>
<body>
    <h1>Daftar Teman</h1>
    <ul>
        {% for nama in teman %}
            <li>{{ nama }}</li>
        {% else %}
            <li>Tidak ada teman</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Sintaks Jinja2 yang Sering Dipakai

| Sintaks | Fungsi | Contoh |
|---|---|---|
| `{{ variabel }}` | Cetak nilai variabel | `{{ nama }}` |
| `{% for x in list %}` | Looping | `{% for item in items %}` |
| `{% endfor %}` | Akhir looping | |
| `{% if kondisi %}` | Percabangan | `{% if user %}...{% endif %}` |
| `{% else %}` | Bagian else dari if/for | |
| `{% endif %}` | Akhir percabangan | |

### Contoh If di Template:

```html
{% if user %}
    <p>Selamat datang, {{ user.nama }}!</p>
{% else %}
    <p>Silakan login terlebih dahulu.</p>
{% endif %}
```


## Template Inheritance (Warisan Template)

Ini fitur paling berguna dari Jinja2. Idenya: buat satu **kerangka** utama,
lalu halaman lain tinggal mengisi bagian yang berbeda.

### base.html (Kerangka Utama)

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Aplikasiku{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Beranda</a>
        <a href="/tentang">Tentang</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

`{% block nama %}` adalah "lubang" yang bisa diisi oleh halaman lain.

### index.html (Mewarisi base.html)

```html
{% extends 'base.html' %}

{% block title %}Beranda{% endblock %}

{% block content %}
    <h1>Halo, {{ nama }}!</h1>
    <p>Ini halaman beranda.</p>
{% endblock %}
```

`{% extends 'base.html' %}` artinya: "Pakai kerangka dari base.html,
lalu isi block-block di bawah ini."

### Keuntungan

- **Konsisten** -- semua halaman punya navbar yang sama
- **Efisien** -- ganti navbar di satu file, semua halaman berubah
- **Rapi** -- tidak perlu mengulang kode HTML yang sama


## Ringkasan

| Langkah | Kode |
|---|---|
| Panggil template | `render_template('file.html', var=nilai)` |
| Cetak variabel | `{{ var }}` |
| Looping | `{% for x in list %}...{% endfor %}` |
| Percabangan | `{% if %}...{% else %}...{% endif %}` |
| Inheritance | `{% extends 'base.html' %}` |
| Definisikan block | `{% block nama %}...{% endblock %}` |
| Isi block | Tulis konten di antara `{% block nama %}` dan `{% endblock %}` |
