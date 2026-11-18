# ============================================
# PROGRAM SEQUENTIAL SEARCH DASAR
# ============================================

def sequential_search(arr, key):
    """
    Melakukan pencarian sekuensial (Sequential Search) pada array.
    """
    print(f"\nMemulai Sequential Search untuk mencari {key} dalam array: {arr}")
    
    for i in range(len(arr)):
        current_value = arr[i]
        print(f"Langkah {i+1}: Membandingkan elemen pada indeks {i} ({current_value}) dengan {key}...")
        
        if current_value == key:
            print(f"Ditemukan! {key} berada pada indeks {i}.")
            return i
    
    print(f"\n{key} tidak ditemukan dalam array.")
    return -1


def main():
    data_array = [10, 30, 50, 70, 20, 80]
    
    while True:
        print("\n" + "="*45)
        print("   PROGRAM ILUSTRASI SEQUENTIAL SEARCH")
        print("="*45)
        print(f"Array data: {data_array}")
        print("-"*45)
        print("1. Cari angka")
        print("2. Ganti array data")
        print("0. Keluar")
        print("-"*45)
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            try:
                search_key = int(input("\nMasukkan angka yang ingin dicari: "))
                hasil = sequential_search(data_array, search_key)
                
                if hasil != -1:
                    print(f"\n>> Hasil Akhir: Angka {search_key} ditemukan pada indeks {hasil}.")
                else:
                    print(f"\n>> Hasil Akhir: Angka {search_key} tidak ditemukan dalam array.")
                    
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
                
        elif pilihan == "2":
            try:
                data_baru = input("Masukkan array baru (pisahkan dengan koma, contoh: 5,10,15): ")
                data_array = [int(x.strip()) for x in data_baru.split(",")]
                print(f"Array berhasil diubah: {data_array}")
            except ValueError:
                print("Input tidak valid.")
                
        elif pilihan == "0":
            print("\nTerima kasih! Program berakhir.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()