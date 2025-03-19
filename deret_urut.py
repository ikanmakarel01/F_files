tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

for i in range(1, tinggi+1):
    for j in range(1, lebar+1):
        print((i-1)*lebar + j, end=" ")
    print()
# expected output for tinggi = 5, lebar = 4
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12

# wanted output for tinggi = 5, lebar = 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 17 18 19 20
#

def print_number_grid(tinggi, lebar):
    num = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(num, end=" ")
            num += 1
        print()  # Pindah ke baris baru

# Input tinggi dan lebar dari pengguna
tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

# Cetak hasilnya
print_number_grid(tinggi, lebar)
