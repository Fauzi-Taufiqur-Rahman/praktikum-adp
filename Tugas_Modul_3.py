print ("TEBAK ANGKA BOM")
print ("Pemain 1")
n = int(input("Masukkan Batas Angka Positif: "))
k = int(input("Masukkan Angka Bom: "))
i = 1
for i in range (1,n+1):
    if i%k == 0 :
        print ("BOM",end=" ")
    else :
        print(i,end=" ")

print ("\nPemain 2")
for i in range (n):
    angka = int(input(f"tebak angka dari 1 - {n}: "))
    if angka%k == 0 and angka <=n :
        print(f"angka {angka} bom, anda kalah!")
        break
    elif angka<1 or angka>n:
        print(f"silakan masukkan angka kembali!")
    else :
        print(f"angka {angka} bukan bom, anda menang!")
        break
print("Permainan Selesai")