# ============================================
# STUDI KASUS 2: VERIFIKASI ITEM KERANJANG
# ============================================

def verifikasi_item_keranjang(keranjang, item_target):
    """
    Memverifikasi keberadaan item di keranjang belanja menggunakan Sequential Search.
    """
    item_target_lower = item_target.lower()
    for item in keranjang:
        if item.lower() == item_target_lower:
            return True
    return False


def main():
    keranjang_belanja = [
        "rx king",
        "vespa matic",
        "vario 125",
        "c70",
        "beat street",
        "zxr 250",
        "supraX 125",
        "ninja 250",
        "honda scoopy",
        "yamaha aerox",
        "kawasaki ninja 150",
        "honda vario 150",
        "suzuki satria FU"
    ]
    
    while True:
        print("\n" + "="*45)
        print("   STUDI KASUS 2: KERANJANG BELANJA")
        print("="*45)
        print("Isi Keranjang Belanja Anda:")
        for i, item in enumerate(keranjang_belanja):
            print(f"  [{i}] {item}")
        print("-"*45)
        print("1. Verifikasi item")
        print("2. Tambah item ke keranjang")
        print("3. Hapus item dari keranjang")
        print("0. Keluar")
        print("-"*45)
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            item_verifikasi = input("\nMasukkan nama item yang ingin diverifikasi: ")
            
            if verifikasi_item_keranjang(keranjang_belanja, item_verifikasi):
                print(f"\n>> Item '{item_verifikasi}' ADA di keranjang belanja Anda.")
            else:
                print(f"\n>> Item '{item_verifikasi}' TIDAK ADA di keranjang belanja Anda.")
                
        elif pilihan == "2":
            item_baru = input("Masukkan nama item baru: ")
            keranjang_belanja.append(item_baru)
            print(f"'{item_baru}' berhasil ditambahkan ke keranjang.")
            
        elif pilihan == "3":
            item_hapus = input("Masukkan nama item yang akan dihapus: ")
            indeks = -1
            for i, item in enumerate(keranjang_belanja):
                if item.lower() == item_hapus.lower():
                    indeks = i
                    break
            
            if indeks != -1:
                dihapus = keranjang_belanja.pop(indeks)
                print(f"'{dihapus}' berhasil dihapus dari keranjang.")
            else:
                print("Item tidak ditemukan.")
                
        elif pilihan == "0":
            print("\nTerima kasih! Program berakhir.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main() 