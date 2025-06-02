def buat_data_awal(nama_file):
    data_buku = [
        ["9786020328919", "Laskar Pelangi", "Andrea Hirata", 15, 55000, 85000],
        ["9789792293453", "Negeri 5 Menara", "Ahmad Fuadi", 10, 60000, 90000],
        ["9789794335007", "Bumi", "Tere Liye", 20, 65000, 95000],
        ["9789793062793", "Ayat-Ayat Cinta", "Habiburrahman El Shirazy", 12, 50000, 80000],
        ["9786024245978", "Ayahku Bukan Pembohong", "Tere Liye", 35, 65000, 85000],
        ["9786021234567", "3726 mdpl", "Fajar Nugraha", 20, 60000, 78000],
        ["9786020942764", "Perahu Kertas", "Dee Lestari", 4, 60000, 90000],
        ["9786020328933", "Sebelas Patriot", "Andrea Hirata", 4, 50000, 80000],
        ["9780439708180", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 45, 75000, 99000],
        ["9786020332176", "Surat Kecil untuk Tuhan", "Agnes Davonar", 7, 48000, 78000]
    ]

    with open(nama_file, 'w') as file:  
        for buku in data_buku:
            file.write(','.join(str(item) for item in buku) + '\n')  


def baca_data_dari_file(nama_file):
    inventaris = {}
    with open(nama_file, 'r') as file:  
        for baris in file:
            if not baris.strip():
                continue
            isbn, judul, penulis, stok, harga_beli, harga_jual = baris.strip().split(',')
            inventaris[isbn] = {
                'Judul': judul,
                'Penulis': penulis,
                'Stok': int(stok),
                'Harga Beli': int(harga_beli),
                'Harga Jual': int(harga_jual),
            }
    return inventaris


def hitung_potensi_untung(inventaris):
    for data in inventaris.values():
        data['Potensi Keuntungan'] = (data['Harga Jual'] - data['Harga Beli']) * data['Stok']
    return inventaris


def simpan_laporan(inventaris, nama_file):
    with open(nama_file, 'w') as file:
        file.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
        for isbn, data in inventaris.items():
            file.write(f"{isbn},{data['Judul']},{data['Penulis']},{data['Stok']},"
                       f"{data['Harga Beli']},{data['Harga Jual']},{data['Potensi Keuntungan']}\n")


def analisis_inventaris(inventaris):
    buku_tertinggi = None
    buku_terendah = None

    for isbn, data in inventaris.items():
        if buku_tertinggi is None or data['Potensi Keuntungan'] > inventaris[buku_tertinggi]['Potensi Keuntungan']:
            buku_tertinggi = isbn
        if buku_terendah is None or data['Potensi Keuntungan'] < inventaris[buku_terendah]['Potensi Keuntungan']:
            buku_terendah = isbn

    print("\nBuku dengan potensi keuntungan TERTINGGI:")
    print(f"{inventaris[buku_tertinggi]['Judul']} - Rp{inventaris[buku_tertinggi]['Potensi Keuntungan']:,}")

    print("\nBuku dengan potensi keuntungan TERENDAH:")
    print(f"{inventaris[buku_terendah]['Judul']} - Rp{inventaris[buku_terendah]['Potensi Keuntungan']:,}")

    total_nilai_inventaris = 0
    for data in inventaris.values():
        total_nilai_inventaris += data['Stok'] * data['Harga Beli']
    print(f"\nTotal Nilai Inventaris: Rp{total_nilai_inventaris:,}")

    print("\nDaftar buku dengan stok kurang dari 5 (perlu restock):")
    ada_restock = False
    for data in inventaris.values():
        if data['Stok'] < 5:
            print(f"- {data['Judul']} (Stok: {data['Stok']})")
            ada_restock = True
    if not ada_restock:
        print("Tidak ada buku yang perlu restock.")

nama_file_input = "inventaris_buku.txt"
nama_file_output = "laporan_inventaris.txt"
buat_data_awal(nama_file_input)
inventaris = baca_data_dari_file(nama_file_input)
inventaris = hitung_potensi_untung(inventaris)
simpan_laporan(inventaris, nama_file_output)
analisis_inventaris(inventaris)
