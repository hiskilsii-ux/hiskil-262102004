import math

print("==Progam Lingkaran==")
print("1. Hitung Keliling Lingkaran")
print("2. Hitung Luas Lingkaran")

pilihan = int(input("Masukkan pilihan (1/2): "))
r = float(input("Masukkan jari-jari: "))

if pilihan == 1:
    keliling = 2 * math.pi * r
    print("Keliling lingkaran =",round(keliling, 2))
elif pilihan == 2:
    luas = math.pi * r**2
    print("Luas lingkaran =",round(luas, 2))
else:
    print("Pilihan tidak valid. Masukakan angka 1 atau 2.")