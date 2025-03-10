#Input Data Diri
print("Masukkan data diri anda!")
Nama                =str(input("Masukkan Nama Anda     :"))
Umur                =int(input("Masukkan Umur Anda     :"))
Jenis_Kelamin       =str(input("Masukkan Jenis Kelamin :"))
#Memilih Kode Maskapai
print ("Pilih Kode Maskapai!")
print ("3012 : Padang-Jakarta")
print ("4015 : Padang-Batam")
print ("4050 : Padang-Bandung")
Kode_Maskapai       = int(input("Pilih Kode Maskapai   :"))
#Menampilkan menu jenis Maskapai
if Kode_Maskapai    == 3012 :
    print ("Ekonomi        : Rp800.000")
    print ("Bisnis         : Rp850.000")
    print ("First Class    : Rp900.000")
elif Kode_Maskapai  == 4015 :
    print ("Ekonomi        : Rp500.000")
    print ("Bisnis         : Rp550.000")
    print ("First Class    : Rp700.000")
elif Kode_Maskapai  == 4050 :
    print ("Ekonomi        : Rp700.000")
    print ("Bisnis         : Rp750.000")
    print ("First Class    : Rp850.000")
Jenis               = input("Masukkan Jenis Maskapai   :")
Tiket               = int(input("Masukkan Jumlah Tiket :"))
if Tiket>3                 :
    print("Mendapatkan diskon sebesar 20%")
#Menampilkan Struk Pemesanan
print("------STRUK PEMESANAN------")
print(f"Nama               : {Nama}")
print(f"Umur               : {Umur}")
print(f"Jenis Kelamin      : {Jenis_Kelamin}")
print("---------------------------")
print(f"Kode Maskapai      : {Kode_Maskapai}")

if Kode_Maskapai    ==3012 :
    print("Tujuan Maskapai    : Padang-Jakarta")
elif Kode_Maskapai  ==4015 :
    print("Tujuan Maskapai    : Padang-Batam")
elif Kode_Maskapai  ==4050 :
    print("Tujuan Maskapai    : Padang-Bandung")

print (f"Jenis Maskapai     : {Jenis}")
print (f"Jumlah Tiket       : {Tiket}")

if Kode_Maskapai    ==3012 and Jenis =="Ekonomi":
    harga           =800000
elif Kode_Maskapai  ==3012 and Jenis =="Bisnis":
    harga           =850000
elif Kode_Maskapai  ==3012 and Jenis =="First Class":
    harga           =900000
if Kode_Maskapai    ==4015 and Jenis =="Ekonomi":
    harga           =500000
elif Kode_Maskapai  ==4015 and Jenis =="Bisnis":
    harga           =550000
elif Kode_Maskapai  ==4015 and Jenis =="First Class":
    harga           =700000
if Kode_Maskapai    ==4050 and Jenis =="Ekonomi":
    harga           =700000
elif Kode_Maskapai  ==4050 and Jenis =="Bisnis":
    harga           =750000
elif Kode_Maskapai  ==4050 and Jenis =="First Class":
    harga           =850000
Harga           = Tiket*harga 
if Tiket>3:
    Harga           = (Harga)-(Harga*0.2)
Total               = Harga
print(f"Total Harga        : Rp{Total}")
print("--------TERIMAKASIH--------")