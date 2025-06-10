from os import system as clear
from time import sleep
from termcolor import cprint

# Logo Roblox versi ASCII (lubang tengah bergaya diamond)
roblox_logo = [
    "        #######        ",
    "      ###########      ",
    "     ####     ####     ",
    "    ####       ####    ",
    "   ####         ####   ",
    "  ####           ####  ",
    " ####             #### ",
    "####               ####",
    " ####             #### ",
    "  ####           ####  ",
    "   ####         ####   ",
    "    ####       ####    ",
    "     ####     ####     ",
    "      ###########      ",
    "        #######        ",
]

# Bersihkan layar
clear("cls")

# Tampilkan logo baris per baris (animasi masuk)
for row in roblox_logo:
    for char in row:
        if char == "#":
            cprint(" ", on_color="on_red", end="")
        else:
            print(" ", end="")
    print()
    sleep(0.1)

# Loading muncul di bawah logo
for i in range(101):
    print(' ' * 20, end='')  # indentasi
    cprint(f"Loading...{i}%", "red", attrs=['bold'], end='\r')
    sleep(0.05)

# Pindah baris agar loading tidak tertimpa
print()
cprint("Berhasil Memuat Game!".center(70), "white", "on_red", attrs=['bold'])

sleep(2)
clear("cls")
