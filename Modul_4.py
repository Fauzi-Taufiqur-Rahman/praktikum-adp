while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))

    if r>=4 and c>=4:
        break
    else:
        print ("Ukuran minimal bioskop adalah 4X4! Silakan masukkan ulang.")

terisi = str(" ")
total = r * c

while True:
    print ("Layout Kursi: ")
    nomor = 1
    for i in range (r):
        for j in range (c):
            kursi = str (nomor)
            if " " + kursi + " " in terisi:
                print ("X", end=" ")
            else:
                print (kursi, end=" ")
            nomor += 1
        print ()
    pesan = input("\nMasukkan nomor kursi yang ingin dipesan (atau ketik '0' untuk selesai): ")
    if pesan == "0" :
        print ("Terima kasih telah memesan tiket!")
        break
    pilih = int(pesan)
    if pilih >= 1 and pilih <= total:
        if " " + pesan + " " in terisi :
            print ("Kursi sudah dipesan! Pilih kursi lain")
        else:
            terisi += pesan + " "
            print("Kursi Nomor", pesan, "berhasil dipesan!")
    else:
        print(f"Nomor kursi tidak valid! Masukkan nomor kursi yang tersedia.")