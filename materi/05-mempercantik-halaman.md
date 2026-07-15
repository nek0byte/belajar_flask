# 05 -- Mempercantik Halaman dengan CSS

## Tujuan Pembelajaran

- Membuat file CSS untuk mempercantik halaman
- Menghubungkan file CSS dari template HTML
- Memahami cara Flask menyajikan file statis

Tidak ada logika Python baru di sini. Murni tentang bagaimana Flask
menangani file-file statis seperti CSS, gambar, dan JavaScript.


## Analogi: Baju untuk Website

Bayangkan HTML adalah **kerangka tubuh manusia**:
- Ada kepala, badan, tangan, kaki
- Fungsional, tapi tidak menarik

CSS adalah **baju** yang dikenakan:
- Warna, motif, ukuran
- Membuat penampilan lebih menarik
- Bisa diganti-ganti tanpa mengubah tubuh

Website tanpa CSS:
```
Halo, Dunia!
Selamat datang.
```
(teks hitam di background putih, membosankan)

Website dengan CSS:
```
[teks biru di background abu-abu, rapi, modern]
```


## Masalah: File Statis

Flask harus bisa menyajikan file CSS, gambar, JavaScript ke browser.
Masalahnya, file-file ini tidak diproses oleh Python -- mereka langsung
dikirim ke browser apa adanya. Karena itu disebut **file statis**.

Flask menyediakan folder khusus untuk ini: folder `static/`.

### Struktur Folder

```
board/
├── static/              <-- file statis (CSS, gambar, JS)
│   └── style.css
├── templates/           <-- file HTML
│   └── index.html
├── __init__.py
└── routes.py
```

### Cara Memanggil File Statis di HTML

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

`url_for('static', filename='style.css')` akan menghasilkan URL:
`/static/style.css`.

Flask otomatis melayani file di `/static/xxx` tanpa perlu route khusus.


## Praktik: Membuat CSS

Buat file `board/static/style.css`:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #333366;
}

nav {
    background-color: #333366;
    padding: 10px 20px;
    margin: -20px -20px 20px -20px;
}

nav a {
    color: white;
    text-decoration: none;
    margin-right: 20px;
}

nav a:hover {
    text-decoration: underline;
}

.flash {
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 5px;
}

.flash.success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.flash.error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.message-card {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 15px;
}

.message-card h3 {
    margin-top: 0;
    color: #333366;
}

.btn {
    display: inline-block;
    background-color: #333366;
    color: white;
    padding: 8px 16px;
    text-decoration: none;
    border-radius: 5px;
    border: none;
    cursor: pointer;
}

.btn:hover {
    background-color: #444488;
}

.empty {
    color: #888;
    font-style: italic;
}
```

Penjelasan aturan CSS di atas:

| Aturan | Arti |
|---|---|
| `body { font-family: Arial; }` | Gunakan font Arial untuk seluruh halaman |
| `background-color: #f0f0f0` | Warna latar abu-abu muda |
| `color: #333366` | Warna teks biru gelap |
| `.message-card { ... }` | Gaya untuk setiap kartu pesan (titik = class) |
| `#ddd` | Warna abu-abu untuk border |
| `border-radius: 5px` | Sudut yang melengkung |

> **CSS tidak diajarkan di sini.** Jika belum tahu CSS, cukup copy-paste
> dulu. Nanti pelajari CSS terpisah.
>
> Yang penting untuk Flask: **bagaimana menghubungkan CSS ke HTML**.

### Hubungkan CSS ke base.html

Edit `board/templates/base.html`:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Message Board{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    ...
</body>
</html>
```

Dengan menaruh link CSS di `base.html`, **semua** halaman yang mewarisi
`base.html` akan otomatis menggunakan CSS yang sama.


## Menambahkan Gambar

Selain CSS, folder `static/` juga bisa berisi gambar:

```
board/static/
├── style.css
├── logo.png          <-- taruh gambar di sini
└── images/
    └── background.jpg
```

Panggil di HTML:

```html
<img src="{{ url_for('static', filename='logo.png') }}" alt="Logo">
```

Atau untuk gambar di subfolder:

```html
<img src="{{ url_for('static', filename='images/background.jpg') }}" alt="">
```


## Ringkasan

| Konsep | Penjelasan |
|---|---|
| Folder `static/` | Tempat menyimpan file statis (CSS, gambar, JS) |
| `url_for('static', filename='...')` | Membuat URL ke file statis |
| Flask serve otomatis | Tidak perlu route khusus untuk file statis |
| CSS di `base.html` | Sekali pasang, semua halaman kena |

Yang penting: **Flask secara otomatis melayani file dari folder `static/`**.
Kamu cukup menaruh file di sana dan memanggilnya dengan `url_for('static', ...)`.
