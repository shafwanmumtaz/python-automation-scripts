# ============================================
# STUDI KASUS 1: PENCARIAN NAMA KARYAWAN
# ============================================

def sequential_search_case_insensitive(arr, target):
    """
    Melakukan pencarian sekuensial pada list string secara case-insensitive.
    """
    target_lower = target.lower()
    for i in range(len(arr)):
        if arr[i].lower() == target_lower:
            return i
    return -1


def main():
    daftar_absensi = [
        "sule",
        "aisyah", 
        "yana",
        "dinda",
        "dafa",
        "yoko",
        "nunung"
    ]
    
    while True:
        print("\n" + "="*45)
        print("   STUDI KASUS 1: DAFTAR ABSENSI KARYAWAN")
        print("="*45)
        print("Daftar Absensi Hari Ini:")
        for i, nama in enumerate(daftar_absensi):
            print(f"  [{i}] {nama}")
        print("-"*45)
        print("1. Cari nama karyawan")
        print("2. Tambah karyawan")
        print("3. Hapus karyawan")
        print("0. Keluar")
        print("-"*45)
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama_dicari = input("\nMasukkan nama karyawan yang dicari: ")
            indeks = sequential_search_case_insensitive(daftar_absensi, nama_dicari)
            
            if indeks != -1:
                print(f"\n>> Karyawan '{nama_dicari}' ditemukan pada indeks {indeks}.")
                print(f"   Nama asli dalam daftar: '{daftar_absensi[indeks]}'")
                print("   Status: HADIR!")
            else:
                print(f"\n>> Karyawan '{nama_dicari}' tidak ditemukan. Mungkin tidak hadir.")
                
        elif pilihan == "2":
            nama_baru = input("Masukkan nama karyawan baru: ")
            daftar_absensi.append(nama_baru)
            print(f"'{nama_baru}' berhasil ditambahkan.")
            
        elif pilihan == "3":
            nama_hapus = input("Masukkan nama karyawan yang akan dihapus: ")
            indeks = sequential_search_case_insensitive(daftar_absensi, nama_hapus)
            if indeks != -1:
                dihapus = daftar_absensi.pop(indeks)
                print(f"'{dihapus}' berhasil dihapus dari daftar.")
            else:
                print("Nama tidak ditemukan.")
                
        elif pilihan == "0":
            print("\nTerima kasih! Program berakhir.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()