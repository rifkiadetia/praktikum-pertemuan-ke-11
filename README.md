# praktikum-pertemuan-ke-11
Tugas ini dibuat guna memenuhi tugas mata kuliah matematika pengantar pemrograman
# Nama  : Rifki Ade Tia
# Nim   : 312510334
# Kelas : TI.25.C5
# Praktikum: Program Data Mahasiswa (Python)

Deskripsi:
Program sederhana untuk menyimpan dan mengelola daftar mahasiswa (nama, NIM, nilai) menggunakan fungsi.

Fitur:
- tambah(): menambahkan data mahasiswa
- tampilkan(): menampilkan semua data mahasiswa
- hapus(nama): menghapus data berdasarkan nama (pencarian case-insensitive)
- ubah(nama): mengubah data berdasarkan nama

# Flowchart 
[Mulai]
   |
   v
[Tampilkan Menu]
   |
   v
+-------------------------------+
| Pilih: 1 2 3 4 5              |
+-------------------------------+
   |   |    |    |    |
   |   |    |    |    +--> (5) Keluar -> [Selesai]
   |   |    |    |
   |   |    |    +--> (4) Input nama -> Ubah(nama) -> Kembali ke Menu
   |   |    |
   |   |    +--> (3) Input nama -> Hapus(nama) -> Kembali ke Menu
   |   |
   |   +--> (2) Input data -> Tambah() -> Kembali ke Menu
   |
   +--> (1) Tampilkan() -> Kembali ke Menu
