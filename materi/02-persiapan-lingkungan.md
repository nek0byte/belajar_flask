# 02 -- Persiapan Lingkungan

## Tujuan Pembelajaran

- Membuat virtual environment Python
- Mengaktifkan dan menonaktifkan virtual environment
- Menginstall Flask menggunakan pip
- Menjalankan Flask pertama kali

Tidak ada kode aplikasi di sini. Murni setup.


## Analogi: Kotak Alat Kerja

Bayangkan kamu seorang montir. Setiap montir punya **kotak alat** sendiri.
Ada yang isinya kunci pas, obeng, tang.

Sekarang bayangkan kamu bekerja di bengkel yang punya 3 montir. Masing-masing
butuh alat yang berbeda. Montir A butuh kunci ukuran 10, montir B butuh
ukuran 12.

Kalo semua alat dicampur dalam satu kotak besar, akan kacau. Makanya setiap
montir punya **kotak alat masing-masing**.

**Virtual environment (venv)** adalah "kotak alat" untuk proyek Python-mu.
Setiap proyek Python punya venv sendiri, berisi library yang dibutuhkan
proyek itu saja.

Kenapa penting?
- Proyek A butuh Flask versi 2, Proyek B butuh Flask versi 3
- Tanpa venv, kamu cuma bisa punya SATU versi Flask di komputer
- Dengan venv, setiap proyek punya versi library masing-masing


## Langkah 1: Cek Python

Buka terminal/command prompt, ketik:

```bash
python --version
```

Atau jika punya beberapa versi Python:

```bash
python3 --version
```

Pastikan output-nya Python 3.10 atau lebih baru. Jika belum punya Python,
download dan install dari python.org.

Jika sudah muncul versi Python, lanjut ke langkah 2.


## Langkah 2: Buat Folder Proyek

Pilih folder tempat kamu ingin menyimpan proyek. Misal di `Documents`:

```bash
mkdir learn_flask
cd learn_flask
```

Sekarang kamu berada di dalam folder `learn_flask`.


## Langkah 3: Buat Virtual Environment

```bash
python3 -m venv venv
```

Mari kita bedah perintah ini:

| Bagian | Arti |
|---|---|
| `python3` | Panggil Python |
| `-m venv` | Jalankan module `venv` (virtual environment) |
| `venv` | Nama folder yang akan dibuat untuk venv |

Setelah perintah ini, akan muncul folder baru bernama `venv` di dalam
folder proyekmu. Folder ini berisi Python "tiruan" milik proyek ini saja.


## Langkah 4: Aktifkan Virtual Environment

### Di Linux / Mac:

```bash
source venv/bin/activate
```

### Di Windows (Command Prompt):

```bash
venv\Scripts\activate
```

### Di Windows (PowerShell):

```bash
venv\Scripts\Activate.ps1
```

Setelah aktif, kamu akan melihat `(venv)` di awal baris terminal:

```
(venv) user@komputer:~/learn_flask$
```

Tanda `(venv)` ini memberitahu bahwa kamu sedang menggunakan Python dari
dalam virtual environment.

### Cara tahu venv sedang aktif

Coba cek lokasi Python:

```bash
which python
```

Output harus menunjuk ke dalam folder `venv/bin/python`, bukan
`/usr/bin/python`.


## Langkah 5: Install Flask

Setelah venv aktif, install Flask:

```bash
pip install flask
```

`pip` adalah manajer package Python. Dia akan mendownload dan menginstall
Flask beserta library yang dibutuhkan Flask.

Untuk melihat apa saja yang terinstall:

```bash
pip list
```

Kamu akan melihat Flask dan beberapa library lain yang dibutuhkan Flask
secara otomatis (seperti Jinja2, Werkzeug, Click).


## Langkah 6: Matikan Virtual Environment

Jika sudah selesai bekerja, kamu bisa keluar dari venv:

```bash
deactivate
```

Tanda `(venv)` akan hilang. Kamu kembali ke Python utama komputer.

**PENTING**: Setiap kali mau belajar Flask, kamu harus aktivasi venv dulu.
Jangan lupa!


## Ringkasan Perintah

| Perintah | Fungsi |
|---|---|
| `python3 -m venv venv` | Buat virtual environment baru |
| `source venv/bin/activate` | Aktifkan venv (Linux/Mac) |
| `venv\Scripts\activate` | Aktifkan venv (Windows CMD) |
| `pip install flask` | Install Flask |
| `pip list` | Lihat daftar library terinstall |
| `deactivate` | Keluar dari venv |
| `python run.py` | Jalankan aplikasi Flask (nanti dipakai) |


## Yang Perlu Diingat

1.  Setiap kali buka terminal baru, kamu harus **aktivasi venv dulu**
2.  Jangan hapus folder `venv/` (kecuali mau bikin ulang)
3.  Jangan commit folder `venv/` ke Git (nanti kita buat `.gitignore`)
4.  Jika error "command not found: pip", coba `pip3` atau
    `python3 -m pip install flask`
