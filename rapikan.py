#!/usr/bin/env python3
"""
rapikan.py — Skrip Otomasi Pengelompokan File Berdasarkan Kategori Ekstensi
Penyusun: Shafwan Mumtaz
"""

import os
import shutil
import argparse

KATEGORI_FOLDER = {
    "Spreadsheet_dan_Dataset": [".csv", ".xlsx", ".xls"],
    "Dokumen_PDF": [".pdf"],
    "Dokumen_Word_dan_Teks": [".docx", ".doc", ".txt", ".md"],
    "Presentasi": [".pptx", ".ppt"],
    "Koding_dan_Notebook": [".py", ".ipynb", ".java", ".sql", ".html", ".css", ".js", ".json"],
    "Gambar_dan_Media": [".jpg", ".jpeg", ".png", ".webp", ".svg", ".mp4", ".mp3"],
    "Arsip_ZIP_dan_RAR": [".zip", ".rar", ".7z"],
}


def tentukan_kategori(ekstensi: str) -> str:
    ext_lower = ekstensi.lower()
    for nama_folder, daftar_ext in KATEGORI_FOLDER.items():
        if ext_lower in daftar_ext:
            return nama_folder
    return "File_Lainnya"


def pindahkan_aman(src_path: str, dest_dir: str, nama_file: str, dry_run: bool = False) -> str:
    os.makedirs(dest_dir, exist_ok=True)
    base, ext = os.path.splitext(nama_file)
    dest_path = os.path.join(dest_dir, nama_file)
    counter = 1
    while os.path.exists(dest_path):
        dest_path = os.path.join(dest_dir, f"{base}_{counter}{ext}")
        counter += 1

    if not dry_run:
        shutil.move(src_path, dest_path)
    return dest_path


def rapikan_direktori(target_dir: str, dry_run: bool = False):
    if not os.path.isdir(target_dir):
        print(f"[ERROR] Direktori tidak ditemukan: {target_dir}")
        return

    ringkasan = {}
    nama_script_ini = os.path.basename(__file__)

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isdir(item_path) or item == nama_script_ini or item.startswith("."):
            continue

        _, ext = os.path.splitext(item)
        if not ext:
            continue

        kategori = tentukan_kategori(ext)
        folder_tujuan = os.path.join(target_dir, kategori)
        pindahkan_aman(item_path, folder_tujuan, item, dry_run=dry_run)
        ringkasan[kategori] = ringkasan.get(kategori, 0) + 1
        status = "[DRY-RUN]" if dry_run else "[DIPINDAHKAN]"
        print(f"{status} {item} -> {kategori}/")

    print("\n=== Ringkasan Pengelompokan File ===")
    if not ringkasan:
        print("Tidak ada file yang perlu dipindahkan.")
    else:
        for kat, jumlah in sorted(ringkasan.items()):
            print(f"- {kat}: {jumlah} file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Otomasi pengelompokan file ke dalam folder kategori.")
    parser.add_argument("--target", default=".", help="Path direktori yang ingin dirapikan (default: direktori saat ini)")
    parser.add_argument("--dry-run", action="store_true", help="Simulasi tanpa memindahkan file")
    args = parser.parse_args()

    rapikan_direktori(os.path.abspath(args.target), dry_run=args.dry_run)
