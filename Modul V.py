jumlah = int(input("Masukkan jumlah mahasiswa: "))
data_mahasiswa = []
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    pre = float(input("Nilai pretest: "))
    post = float(input("Nilai posttest: "))
    makalah = float(input("Nilai makalah: "))
    nilai = (0.4 * pre) + (0.4 * post) + (0.2 * makalah)
    data_mahasiswa.append([nama, nilai])
print("\nTABEL NILAI MAHASISWA")
print(f"|{"Nama Mahasiswa":<20} | {"Nilai Akhir":<10}|")
print("-" * 36)
for data in data_mahasiswa:
    print(f"|{data[0]:<20} | {data [1]:<10.2f} |")
total = 0
print("-" * 36)
for data in data_mahasiswa:
    total += data[1]
rata_rata = total / jumlah
print(f"Rata-rata nilai akhir kelas: {rata_rata :.2f}")
tertinggi = data_mahasiswa[0]
terendah = data_mahasiswa[0]
for data in data_mahasiswa:
    if data[1] > tertinggi[1]:
        tertinggi = data
    if data[1] < terendah[1]:
        terendah = data
print(f"\nNilai tertinggi : {tertinggi[0]} dengan nilai {tertinggi[1] :.2f}")
print(f"Nilai terendah : {terendah[0]} dengan nilai {terendah[1] :}")
print("\nMahasiswa dengan nilai di atas rata-rata:")
for data in data_mahasiswa:
    if data[1] > rata_rata:
        print(f"- {data[0]} ({data[1]:.2f})")