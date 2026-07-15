# 01 -- Cara Kerja Web

## Tujuan Pembelajaran

- Apa itu URL dan bagian-bagiannya
- Apa itu HTTP dan fungsinya
- Bedanya request dan response
- Bedanya method GET dan POST
- Apa itu status code


## Analogi: Surat-menyurat

Bayangkan kamu mengirim surat ke temanmu.

- Kamu menulis **alamat** di amplop: tujuan, jalan, kota, kode pos.
- Kamu menulis **isi surat**: apa yang kamu minta atau tanyakan.
- Kantor pos mengantarkan suratmu.
- Temanmu membaca, lalu **membalas** dengan surat balasan.

Ini persis seperti cara kerja web:

- **Alamat** di amplop = **URL** (Uniform Resource Locator)
- **Isi surat** = **Request** (permintaan)
- **Kantor pos** = **Internet**
- **Surat balasan** = **Response** (jawaban)
- **Temanmu** = **Server**


## Apa Itu URL?

URL adalah alamat yang kamu ketik di browser. Contoh:

```
https://www.example.com:8080/beranda?kata=kucing#section2
```

Mari kita bedah satu per satu dari kiri ke kanan:

| Bagian | Contoh | Arti |
|---|---|---|
| **Protocol** | `https://` | Aturan komunikasi. HTTPS = aman, HTTP = biasa |
| **Subdomain** | `www` | Biasanya `www`, bisa diganti `blog`, `api`, dll |
| **Domain** | `example.com` | Nama website. Setiap website punya domain unik |
| **Port** | `:8080` | "Pintu" khusus ke server. 80 untuk HTTP, 443 untuk HTTPS |
| **Path** | `/beranda` | Halaman spesifik di website. Bisa `/tentang`, `/produk/1` |
| **Query** | `?kata=kucing` | Data tambahan yang dikirim via URL. Dimulai dengan `?` |
| **Fragment** | `#section2` | Bagian tertentu dalam halaman. Tidak dikirim ke server |

Kamu tidak harus hafal semua. Yang penting: **URL adalah alamat yang
memberi tahu server "halaman apa yang aku minta".**


## Apa Itu HTTP?

HTTP adalah **bahasa** yang digunakan browser dan server untuk berbicara.

- Browser berkata: "Halo server, saya mau minta halaman `/beranda`"
  (ini namanya **HTTP Request**)
- Server menjawab: "Baik, ini halaman `/beranda`-nya" (ini namanya
  **HTTP Response**)

Kedua duanya menggunakan aturan HTTP agar saling paham.

### Proses Request-Response

```
Browser                          Server
  │                                │
  ├── REQUEST ────────────────────>│
  │   GET /beranda HTTP/1.1        │
  │   Host: www.example.com        │
  │                                │
  │<──_ RESPONSE ──────────────────┤
  │   HTTP/1.1 200 OK              │
  │   Content-Type: text/html      │
  │                                │
  │   <html>... Halaman ...        │
  │   </html>                      │
```

Ini terjadi setiap kali kamu membuka halaman web.


## HTTP Methods (Cara Meminta)

Ada beberapa "kata kerja" HTTP yang berbeda untuk tujuan berbeda:

### GET -- Minta Data

GET digunakan ketika kamu **meminta** sesuatu. Contoh:
- Membuka halaman beranda
- Mencari produk
- Melihat detail pesan

GET menempelkan data di URL. Contoh:

```
www.contoh.com/cari?q=python+flask
```

Ciri-ciri GET:
- Data terlihat di URL
- Bisa di-bookmark
- Tidak cocok untuk mengirim password atau data rahasia
- Tidak boleh digunakan untuk mengubah data (misal: menghapus pesan)

### POST -- Kirim Data

POST digunakan ketika kamu **mengirim** sesuatu. Contoh:
- Mengisi form login
- Mendaftar akun baru
- Membuat pesan baru

POST mengirim data di **body** request, bukan di URL. Jadi:

```
URL: www.contoh.com/login
Body (tidak terlihat): username=budi&password=rahasia
```

Ciri-ciri POST:
- Data tidak terlihat di URL
- Tidak bisa di-bookmark
- Cocok untuk data sensitif
- Dipakai untuk mengubah/menambah data

### Analogi Sederhana

| Situasi | Method HTTP |
|---|---|
| Kamu melihat menu di jendela restoran | GET |
| Kamu masuk dan memesan makanan | POST |
| Kamu memanggil pelayan untuk bertanya | GET |
| Kamu minta ganti pesanan | POST (mengubah data) |


## HTTP Status Codes

Server memberi kode status di response-nya. Ini seperti "kode singkat" yang
memberi tahu browser apakah permintaan berhasil.

| Kode | Arti | Seperti... |
|---|---|---|
| **200** | OK -- Berhasil | "Pesananmu siap" |
| **302** | Redirect -- Pindah halaman | "Maaf, meja kami di lantai 2" (kamu diarahkan) |
| **400** | Bad Request -- Permintaan salah | "Pesananmu tidak jelas, ulangi" |
| **404** | Not Found -- Halaman tidak ada | "Menu itu tidak ada di daftar" |
| **500** | Internal Server Error -- Error di server | "Koki jatuh sakit, maaf" |

Kamu akan sering melihat kode 200 (berhasil), 302 (redirect), 404 (tidak
ditemukan), dan 500 (error server).


## Ringkasan

- **URL** adalah alamat website. Terdiri dari protocol, domain, path, query
- **HTTP** adalah bahasa komunikasi antara browser dan server
- **Request** adalah permintaan dari browser ke server
- **Response** adalah jawaban dari server ke browser
- **GET** untuk meminta data, **POST** untuk mengirim data
- **Status code** memberi tahu apakah permintaan berhasil atau gagal
- Setiap kali kamu buka website, terjadi siklus request-response
