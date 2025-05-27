def input_data():
    jumlah = int(input("Masukkan Jumlah Mahasiswa: "))
    data = []
    for i in range(jumlah):
        print(f"\nData Mahasiswa ke-{i+1}")
        nama = input("Masukkan Nama Mahasiswa: ")
        nim = int(input("Masukkan NIM Mahasiswa: "))
        uts = float(input("Nilai UTS Mahasiswa: "))
        uas = float(input("Nilai UAS Mahasiswa: "))
        tugas = float(input("Nilai Tugas Mahasiswa: "))
        data.append({"nama": nama, "nim": nim, "uts": uts, "uas": uas, "tugas": tugas})
    return data

def rata(data, kunci):
    total = 0
    for mahasiswa in data:
        total += mahasiswa[kunci]
    return total / len(data)

def hitung_nilai(data):
    for mahasiswa in data:
        mahasiswa["nilai_akhir"] = 0.35 * mahasiswa["uts"] + 0.35 * mahasiswa["uas"] + 0.3 * mahasiswa["tugas"]
    return data

def peringkat(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]["nilai_akhir"] < data[j]["nilai_akhir"]:
                data[i], data[j] = data[j], data[i]
    for i in range(len(data)):
        data[i]["peringkat"] = i + 1
    return data

def tabel(data):
    print()
    print("="*112)
    print(f"|| {'Nama':<20} || {'NIM':<10} || {'UTS':<10} || {'UAS':<10} || {'Tugas':<10} || {'Nilai Akhir':<12} || {'Peringkat':<10} ||")
    print("="*112)
    for mahasiswa in data:
        print(f"|| {mahasiswa['nama']:<20} || {mahasiswa['nim']:<10} || {mahasiswa['uts']:<10.2f} || {mahasiswa['uas']:<10.2f} || {mahasiswa['tugas']:<10.2f} || {mahasiswa['nilai_akhir']:<12.2f} || {mahasiswa['peringkat']:<10} ||")

    print("="*112)
    print(f"|| {'Rata-rata':<20} || {'':<10} || {rata(data, 'uts'):<10.2f} || {rata(data, 'uas'):<10.2f} || {rata(data, 'tugas'):<10.2f} || {rata(data, 'nilai_akhir'):<12.2f} || {'':<10} ||")
    print("="*112)

def main():
    data = input_data()
    data = hitung_nilai(data)
    data = peringkat(data)
    tabel(data)

main()