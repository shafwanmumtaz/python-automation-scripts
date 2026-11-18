# Class Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim} | Nama: {self.nama} | Jurusan: {self.jurusan}"


# Fungsi Linear Search
def cari_mahasiswa_linear(daftar_mahasiswa, nim_target):
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.nim == nim_target:
            return mahasiswa
    return None


# Data awal
data_mahasiswa = [
    Mahasiswa("202601", "Shafwan", "Teknik Informatika"),
    Mahasiswa("202602", "Rizal", "Sistem Informasi"),
    Mahasiswa("202603", "Alfiil qory rahman", " Teknik Sipil "),
]


# Fungsi tampil data
def tampilkan_data():
    if not data_mahasiswa:
        print("Data mahasiswa kosong.")
    else:
        print("\n=== DATA MAHASISWA ===")
        for mhs in data_mahasiswa:
            print(mhs)


# Fungsi tambah data
def tambah_mahasiswa():
    print("\n=== TAMBAH MAHASISWA ===")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")

    data_mahasiswa.append(Mahasiswa(nim, nama, jurusan))
    print("✅ Data berhasil ditambahkan!")


# Fungsi cari data
def cari_mahasiswa():
    print("\n=== CARI MAHASISWA ===")
    nim = input("Masukkan NIM yang dicari: ")

    hasil = cari_mahasiswa_linear(data_mahasiswa, nim)

    if hasil:
        print("\n✅ Data ditemukan:")
        print(hasil)
    else:
        print("\n❌ Data tidak ditemukan.")


# Menu utama
while True:
    print("\n===== SISTEM DATA MAHASISWA =====")
    print("1. Tampilkan Data")
    print("2. Tambah Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_mahasiswa()
    elif pilihan == "3":
        cari_mahasiswa()
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid, coba lagi.")