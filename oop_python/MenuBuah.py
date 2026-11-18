def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


data_angka = [15, 22, 10, 30, 5, 88, 7]
daftar_buah = ["Mengkudu", "Terong Belanda", "Alpukat", "Jambu", "Khuldi"]


while True:
    print("\n=== MENU PENCARIAN ===")
    print("1. Cari Angka")
    print("2. Cari Buah")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        try:
            target = int(input("Masukkan angka: "))
            hasil = linear_search(data_angka, target)

            if hasil != -1:
                print(f"✅ Angka ditemukan di indeks ke-{hasil}")
            else:
                print("❌ Angka tidak ditemukan")
        except:
            print("❌ Input harus angka!")

    elif pilihan == "2":
        target = input("Masukkan nama buah: ")
        hasil = linear_search(daftar_buah, target)

        if hasil != -1:
            print(f"✅ Buah ditemukan di indeks ke-{hasil}")
        else:
            print("❌ Buah tidak ditemukan")

    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid")