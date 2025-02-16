
# Program Manajemen Perpustakaan

Program ini adalah sistem manajemen perpustakaan sederhana yang memungkinkan pengguna untuk melihat daftar buku, meminjam/mengembalikan buku, serta mengelola data buku dan anggota.

## Fitur Utama
1. **Menu Tamu**: Pengguna dapat melihat daftar buku tanpa login.
2. **Menu Anggota**: Anggota dapat login, meminjam/mengembalikan buku, dan melihat daftar buku.
3. **Menu Pustakawan**: Admin dapat menambah, memperbarui, dan melihat data buku serta anggota.

---

## Struktur Data Awal

### Daftar Buku
```python
books = [
    {'ISBN': '9780451526342', 'namaBuku': 'Animal Farm', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 8, 'harga': 7000},
    {'ISBN': '9780060850524', 'namaBuku': 'Brave New World', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 2, 'harga': 9500},
    # ... (data buku lainnya)
]
```

### Daftar Anggota
```python
members = [
    {'fullname': 'Danny Permata Simanjuntak', 'username': 'danny123', 'usia': 33, 'jenis_kelamin': 'L', 'borrowed': []}
]
```

### Kategori Buku
```python
KATEGORI_BUKU = {
    "1": "Novel Fiksi",
    "2": "Novel Non-Fiksi",
    "3": "Pengembangan Diri",
    "4": "Sejarah Dunia"
}
```

---

## Fungsi Helper

### `enter_to_continue()`
Meminta pengguna menekan Enter untuk melanjutkan.

### `display_error(message)`
Menampilkan pesan kesalahan.

### `validate_numeric_input(prompt, error_msg)`
Memastikan input pengguna adalah angka.

### `validate_name_input(prompt, error_msg)`
Memastikan input pengguna hanya berisi huruf dan spasi.

### `display_books(book_list)`
Menampilkan daftar buku dalam format tabel menggunakan library `tabulate`.

### `find_book(isbn_or_title)`
Mencari buku berdasarkan ISBN atau judul.

### `sort_books_by_command(book_list, command)`
Mengurutkan daftar buku berdasarkan harga atau judul.

---

## Menu Utama

### `main_menu()`
Menu utama program:
1. **Tamu**: Akses terbatas untuk melihat daftar buku.
2. **Anggota Perpustakaan**: Login atau mendaftar sebagai anggota.
3. **Pustakawan**: Login sebagai admin untuk mengelola buku dan anggota.
4. **Keluar**: Mengakhiri program.

---

## Menu Tamu

### `menu_tamu()`
Menu tamu memungkinkan pengguna untuk:
- **Melihat rak buku**: Menampilkan daftar buku.
- **Mengurutkan buku**: Mengurutkan buku berdasarkan harga atau judul.

---

## Menu Anggota Perpustakaan

### `menu_anggota_perpustakaan()`
Menu anggota memungkinkan pengguna untuk:
- **Login**: Masuk sebagai anggota.
- **Daftar Anggota Baru**: Mendaftar sebagai anggota baru.
- **Logout**: Keluar dari sesi anggota.

---

## Menu Pustakawan

### `menu_pustakawan()`
Menu pustakawan memungkinkan admin untuk:
- **Cek data buku**: Melihat daftar buku.
- **Menambah buku baru**: Menambahkan buku ke perpustakaan.
- **Mengupdate data buku**: Memperbarui stok atau harga buku.
- **Melihat data anggota**: Menampilkan daftar anggota.
- **Melihat buku yang dipinjam**: Menampilkan daftar buku yang sedang dipinjam.

---

## Proses Peminjaman Buku

### `pinjam_buku()`
Proses peminjaman buku:
1. Pengguna memilih buku berdasarkan ISBN atau judul.
2. Jika buku tersedia, jumlah stok dikurangi, dan buku ditambahkan ke daftar peminjaman anggota.
3. Pengguna harus membayar total harga buku sebelum transaksi selesai.

---

## Proses Pengembalian Buku

### `kembalikan_buku()`
Proses pengembalian buku:
1. Pengguna melihat daftar buku yang dipinjam.
2. Pengguna dapat memilih buku tertentu untuk dikembalikan atau mengembalikan semua buku sekaligus.
3. Stok buku diperbarui, dan buku dihapus dari daftar peminjaman anggota.

---

## Penambahan dan Pembaruan Buku

### `tambah_buku()`
Pustakawan dapat menambahkan buku baru dengan memasukkan detail seperti ISBN, nama, kategori, stok, dan harga.

### `update_buku()`
Pustakawan dapat memperbarui stok atau harga buku yang sudah ada.

---

## Eksekusi Program

Program dijalankan dengan memanggil fungsi `main_menu()` di bagian akhir kode:
```python
if __name__ == "__main__":
    main_menu()
```

---

## Cara Menjalankan Program
1. Pastikan Anda telah menginstal Python dan library `tabulate`.
2. Simpan file ini dengan ekstensi `.py` (misalnya `library_management.py`).
3. Jalankan program menggunakan perintah:
   ```bash
   python library_management.py
   ```

---
