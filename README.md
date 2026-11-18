# Skrip Otomasi Direktori File (`rapikan.py`) & Kumpulan Program Python

👤 **Penyusun:** Shafwan Mumtaz (S1 Teknik Informatika, Universitas Pamulang)  
🐍 **Bahasa & Modul:** Python 3 (`os`, `shutil`, Algoritma Pencarian, & Pemrograman Berorientasi Objek)

---

## 1. Skrip Otomasi Pengelompokan File (`rapikan.py`)

Saat mengerjakan banyak proyek analisis data dan tugas perkuliahan, direktori kerja (`Downloads` / `Documents`) sering kali dipenuhi berbagai ekstensi file yang bercampur (dataset `.csv`/`.xlsx`, dokumen `.pdf`/`.docx`, kode `.py`/`.ipynb`, gambar, dan arsip `.zip`).

Skrip **`rapikan.py`** menggunakan modul bawaan Python (`os` dan `shutil`) untuk:
- Memindai seluruh file di dalam direktori target secara otomatis.
- Mengklasifikasikan file berdasarkan ekstensinya ke dalam folder kategori terstandarisasi (`Spreadsheet_Excel`, `Dokumen_PDF`, `Dokumen_Word`, `Koding_dan_Project`, `Gambar_dan_Media`, `Arsip_ZIP`).
- Menghindari penimpaan file (*collision safe*) apabila terdapat nama file yang sama di folder tujuan.

### Cara Menjalankan `rapikan.py`:
```bash
# Simulasi (Dry-Run) tanpa memindahkan file
python rapikan.py --target "C:/Users/Nama/Downloads" --dry-run

# Menjalankan pengelompokan file secara langsung
python rapikan.py --target "C:/Users/Nama/Downloads"
```

---

## 2. Kumpulan Program Algoritma & OOP Python

Selain skrip otomasi, repositori ini juga memuat program latihan algoritma dan pemrograman Python yang saya kerjakan:

- **`sequential_search/`**:
  - `sequential_search_dasar.py` — Implementasi dasar algoritma *Sequential Search* (pencarian beruntun) pada struktur data *list*.
  - `Absen_Karyawan.py` — Studi kasus pencarian data kehadiran karyawan menggunakan *Sequential Search*.
  - `Belanja_Motor.py` — Program pencarian katalog & simulasi transaksi sederhana.
- **`oop_python/`**:
  - `ClassMahasiswa.py` — Implementasi *Class*, *Object*, dan metode pengelolaan data mahasiswa.
  - `ClassProduk.py` — Implementasi *Class* untuk manajemen inventaris produk dan harga.
  - `MenuBuah.py` — Program interaktif berbasis menu CLI untuk pengelolaan daftar item.
