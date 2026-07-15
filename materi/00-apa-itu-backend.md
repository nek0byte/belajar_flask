# 00 -- Apa Itu Backend Development?

## Tujuan Pembelajaran

- Apa bedanya frontend dan backend
- Gambaran besar bagaimana sebuah website bekerja
- Apa tugas seorang backend developer
- Kenapa kamu perlu belajar backend

Tidak ada kode di materi ini. Murni konsep.


## Analogi: Restoran

Bayangkan kamu pergi ke restoran.

- Kamu adalah **pengunjung**. Kamu hanya mau makan.
- Ada **pelayan** yang datang ke mejamu, membawakan menu, mencatat pesanan,
  dan mengantarkan makanan.
- Ada **koki** di dapur yang memasak makananmu. Kamu tidak melihat koki
  secara langsung, tapi makananmu ada di tangan koki.

Sekarang, bayangkan ini adalah sebuah website:

- Kamu adalah **pengguna** yang membuka website di browser.
- **Browser** (Chrome, Firefox) adalah pelayan yang menampilkan halaman
  kepadamu atau menampilkan bagian Frontend dari website. 
- **Backend** adalah koki di dapur yang menyiapkan data yang kamu minta.

| Restoran | Website |
|---|---|
| Pengunjung | Pengguna / User |
| Pelayan | Browser / Frontend |
| Menu makanan | Tampilan website (HTML, CSS) |
| Koki di dapur | Backend (server + database) |
| Makanan jadi | Halaman web yang kamu lihat |

**Backend adalah "koki" yang bekerja di balik layar.**


## Frontend vs Backend

### Frontend (Yang Terlihat)

Frontend adalah bagian website yang kamu lihat dan interaksi langsung.
Warnanya, tombolnya, animasinya, formnya -- semuanya frontend.

Frontend menggunakan:
- **HTML** untuk struktur (judul, paragraf, gambar)
- **CSS** untuk tampilan (warna, ukuran, tata letak)
- **JavaScript** untuk interaksi (klik, geser, animasi)

### Backend (Yang Tidak Terlihat)

Backend adalah bagian yang bekerja di server, bukan di browsermu.
Dia yang:
- Menyimpan data pengguna ke database
- Memeriksa apakah password yang kamu masukkan benar
- Mengirimkan daftar pesan yang diminta
- Memproses pembayaran

Backend menggunakan bahasa seperti:
- Python (yang kamu pelajari)
- JavaScript (Node.js)
- Java, PHP, Ruby, Go, dan lain-lain

### Analogi Sederhana

Buka aplikasi Instagram:
- **Frontend**: Tampilan feed, tombol like, kotak komentar, warna biru-nya
- **Backend**: Data foto-foto dari temanmu, jumlah like, komentar yang
  tersimpan di database, siapa yang login

Kamu bisa mengganti warna Instagram (frontend) tanpa mengubah cara kerja
suka-menyuka (backend). Sebaliknya, kamu bisa mengubah algoritma rekomendasi
(backend) tanpa mengubah tampilannya (frontend).


## Apa Yang Terjadi Saat Kamu Buka Website?

Ini alur sederhana ketika kamu mengetik `www.contoh.com` di browser:

1.  **Browser** mengirim permintaan ke server `contoh.com`
2.  **Server** (komputer tempat website disimpan) menerima permintaan itu
3.  **Backend** (kode Python/Flask di server) memproses permintaan:
    - "Halaman apa yang diminta?"
    - "Data apa yang perlu diambil dari database?"
4.  **Backend** mengirim balik halaman HTML (lengkap dengan data) ke browser
5.  **Browser** menampilkan halaman itu kepadamu

Semua ini terjadi dalam hitungan detik.


## Apa Tugas Backend Developer?

Seorang backend developer bertanggung jawab atas:

| Tugas | Penjelasan |
|---|---|
| Membuat API | Menyediakan data yang bisa diminta oleh frontend |
| Mengelola database | Menyimpan, mengambil, mengubah, menghapus data |
| Autentikasi | Memastikan hanya pengguna yang sah yang bisa masuk |
| Logika bisnis | Aturan-aturan aplikasi (contoh: "jika saldo kurang dari 0, tolak transaksi") |
| Keamanan | Melindungi data pengguna dari peretas |
| Performa | Memastikan server tidak lambat walau banyak pengguna |

Kesimpulannya: **backend developer membuat "mesin" yang menggerakkan website.**



## Ringkasan

- Backend adalah bagian server yang tidak terlihat oleh pengguna
- Frontend adalah tampilan yang kamu lihat di browser
- Backend bertugas menyimpan data, memproses permintaan, dan mengirim
  response
- Flask adalah framework Python untuk membuat backend
- Kamu akan belajar membuat "koki" (backend) untuk websitemu sendiri
