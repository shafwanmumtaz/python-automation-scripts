# Class Produk
class Produk:
    def __init__(self, sku, nama_produk, stok):
        self.sku = sku
        self.nama_produk = nama_produk
        self.stok = stok

    def __str__(self):
        return f"SKU: {self.sku} | Nama Produk: {self.nama_produk} | Stok: {self.stok}"


# Fungsi Linear Search
def cari_produk_linear(daftar_produk, sku_target):
    for produk in daftar_produk:
        if produk.sku == sku_target:
            return produk
    return None


# Data awal produk
data_produk = [
    Produk("XRP-001", "Honda Civic ", 5),
    Produk("XRP-002", " GTR 86 ", 12),
    Produk("XRP-003", " Mini cooper ", 3),
]


# Fungsi tampil data
def tampilkan_produk():
    if not data_produk:
        print("Data produk kosong.")
    else:
        print("\n=== DATA PRODUK ===")
        for p in data_produk:
            print(p)


# Fungsi tambah produk
def tambah_produk():
    print("\n=== TAMBAH PRODUK ===")
    sku = input("Masukkan SKU: ")
    nama = input("Masukkan Nama Produk: ")
    stok = int(input("Masukkan Stok: "))

    data_produk.append(Produk(sku, nama, stok))
    print("✅ Produk berhasil ditambahkan!")


# Fungsi cari produk
def cari_produk():
    print("\n=== CARI PRODUK ===")
    sku = input("Masukkan SKU yang dicari: ")

    hasil = cari_produk_linear(data_produk, sku)

    if hasil:
        print("\n✅ Produk ditemukan:")
        print(hasil)
    else:
        print("\n❌ Produk tidak ditemukan.")


# Menu utama
def menu():
    while True:
        print("\n===== SISTEM GUDANG PRODUK =====")
        print("1. Tampilkan Produk")
        print("2. Tambah Produk")
        print("3. Cari Produk")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            tambah_produk()
        elif pilihan == "3":
            cari_produk()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid!")


# Menjalankan program
if __name__ == "__main__":
    menu()