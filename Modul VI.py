while True:
    print("Masukkan ukuran matriks A:")
    barisA = int(input("Jumlah baris A: "))
    kolomA = int(input("Jumlah kolom A: "))

    print("Masukkan ukuran matriks B:")
    barisB = int(input("Jumlah baris B: "))
    kolomB = int(input("Jumlah kolom B: "))

    print("Masukkan elemen matriks A:")
    A = []
    for i in range(barisA):
        baris = []
        for j in range(kolomA):
            baris.append(int(input(f"A[{i}][{j}]: ")))
        A.append(baris)

    print("Masukkan elemen matriks B:")
    B = []
    for i in range(barisB):
        baris = []
        for j in range(kolomB):
            baris.append(int(input(f"B[{i}][{j}]: ")))
        B.append(baris)

    while True:
        print("\nMenu Kalkulator Matriks:")
        print("1. Penjumlahan matriks")
        print("2. Pengurangan matriks")
        print("3. Perkalian matriks")
        print("4. Determinan matriks (2x2 atau 3x3)")
        print("5. Invers matriks (2x2)")
        print("6. Transpose matriks")

        p = input("Pilih operasi (1-6): ")

        if p == "1":
            if barisA != barisB or kolomA != kolomB:
                print("Penjumlahan hanya untuk matriks dengan ukuran sama!")
            else:
                print("Hasil Penjumlahan Matriks A + B:")
                for i in range(barisA):
                    print([A[i][j] + B[i][j] for j in range(kolomA)])

        elif p == "2":
            if barisA != barisB or kolomA != kolomB:
                print("Pengurangan hanya untuk matriks dengan ukuran sama!")
            else:
                print("Hasil Pengurangan Matriks A - B:")
                for i in range(barisA):
                    print([A[i][j] - B[i][j] for j in range(kolomA)])

        elif p == "3":
            if kolomA != barisB:
                print("Perkalian tidak bisa dilakukan: kolom A ≠ baris B")
            else:
                print("Hasil Perkalian Matriks A x B:")
                C = []
                for i in range(barisA):
                    baris_C = []
                    for j in range(kolomB):
                        jumlah = 0
                        for k in range(kolomA):
                            jumlah += A[i][k] * B[k][j]
                        baris_C.append(jumlah)
                    C.append(baris_C)
                for row in C:
                    print(row)

        elif p == "4":
            if barisA == kolomA and (barisA == 2 or barisA == 3):
                if barisA == 2:
                    detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
                    print("Determinan Matriks A:", detA)
                else:
                    detA = (
                        A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) -
                        A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) +
                        A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
                    )
                    print("Determinan Matriks A:", detA)
            else:
                print("Determinan hanya untuk matriks persegi ukuran 2x2 atau 3x3")

            if barisB == kolomB and (barisB == 2 or barisB == 3):
                if barisB == 2:
                    detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
                    print("Determinan Matriks B:", detB)
                else:
                    detB = (
                        B[0][0]*(B[1][1]*B[2][2] - B[1][2]*B[2][1]) -
                        B[0][1]*(B[1][0]*B[2][2] - B[1][2]*B[2][0]) +
                        B[0][2]*(B[1][0]*B[2][1] - B[1][1]*B[2][0])
                    )
                    print("Determinan Matriks B:", detB)

        elif p == "5":
            if barisA == kolomA == 2:
                detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
                if detA == 0:
                    print("Matriks A tidak memiliki invers (determinan 0)")
                else:
                    print("Invers Matriks A:")
                    print([
                        round(A[1][1]/detA, 2), round(-A[0][1]/detA, 2)
                    ])
                    print([
                        round(-A[1][0]/detA, 2), round(A[0][0]/detA, 2)
                    ])
            else:
                print("Invers A hanya untuk matriks 2x2")

            if barisB == kolomB == 2:
                detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
                if detB == 0:
                    print("Matriks B tidak memiliki invers (determinan 0)")
                else:
                    print("Invers Matriks B:")
                    print([
                        round(B[1][1]/detB, 2), round(-B[0][1]/detB, 2)
                    ])
                    print([
                        round(-B[1][0]/detB, 2), round(B[0][0]/detB, 2)
                    ])
            else:
                print("Invers B hanya untuk matriks 2x2")

        elif p == "6":
            print("Transpose Matriks A:")
            for j in range(kolomA):
                print([A[i][j] for i in range(barisA)])

            print("Transpose Matriks B:")
            for j in range(kolomB):
                print([B[i][j] for i in range(barisB)])


        else:
            print("Pilihan tidak valid!")
            break

    ulang = input("\nIngin menggunakan kalkulator matriks lagi? (y/n): ")
    if ulang.lower() != "y":
        break