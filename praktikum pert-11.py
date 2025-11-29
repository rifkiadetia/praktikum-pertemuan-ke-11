print("NAMA  : RIFKI ADE TIA")
print("NIM   : 312510334")
print("KELAS : TI.25.C5")
# mahasiswa.py
import sys

# struktur data: list of dict
mahasiswa = [
    {"nama": "Rifki Ade Tia", "nim": "312510334", "nilai": 95},
]

def tambah():
    nama = input("Masukkan nama: ").strip()
    nim = input("Masukkan NIM: ").strip()
    try:
        nilai = float(input("Masukkan nilai: ").strip())
    except ValueError:
        print("Nilai harus angka. Batal menambah.")
        return
    mahasiswa.append({"nama": nama, "nim": nim, "nilai": nilai})
    print(f"Data {nama} berhasil ditambahkan.")

def tampilkan():
    if not mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    print("-" * 40)
    print(f"{'No':<4}{'Nama':<15}{'NIM':<10}{'Nilai':>6}")
    print("-" * 40)
    for i, m in enumerate(mahasiswa, start=1):
        print(f"{i:<4}{m['nama']:<15}{m['nim']:<10}{m['nilai']:>6}")
    print("-" * 40)

def cari_index_by_nama(nama):
    """Kembalikan index pertama yang cocok berdasarkan nama (case-insensitive) atau None."""
    for i, m in enumerate(mahasiswa):
        if m["nama"].lower() == nama.lower():
            return i
    return None

def hapus(nama):
    idx = cari_index_by_nama(nama)
    if idx is None:
        print(f"Tidak ditemukan mahasiswa dengan nama '{nama}'.")
        return False
    removed = mahasiswa.pop(idx)
    print(f"Data {removed['nama']} berhasil dihapus.")
    return True

def ubah(nama):
    idx = cari_index_by_nama(nama)
    if idx is None:
        print(f"Tidak ditemukan mahasiswa dengan nama '{nama}'.")
        return False
    m = mahasiswa[idx]
    print("Biarkan kosong jika tidak ingin mengubah field.")
    new_nama = input(f"Nama [{m['nama']}]: ").strip()
    new_nim  = input(f"NIM  [{m['nim']}]: ").strip()
    new_nilai_str = input(f"Nilai[{m['nilai']}]: ").strip()

    if new_nama:
        m['nama'] = new_nama
    if new_nim:
        m['nim'] = new_nim
    if new_nilai_str:
        try:
            m['nilai'] = float(new_nilai_str)
        except ValueError:
            print("Input nilai tidak valid, nilai tidak diubah.")
    mahasiswa[idx] = m
    print(f"Data {m['nama']} berhasil diperbarui.")
    return True

def menu():
    while True:
        print("\n=== APLIKASI DATA MAHASISWA ===")
        print("1. Tampilkan data")
        print("2. Tambah data")
        print("3. Hapus data (berdasarkan nama)")
        print("4. Ubah data (berdasarkan nama)")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tampilkan()
        elif pilihan == "2":
            tambah()
        elif pilihan == "3":
            nama = input("Masukkan nama yang akan dihapus: ").strip()
            hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang akan diubah: ").strip()
            ubah(nama)
        elif pilihan == "5":
            print("Keluar. Selesai.")
            sys.exit(0)
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()