#contoh output n = 6
#720 6 5 4 3 2 1
#120 5 4 3 2 1
#24 4 3 2 1
#6 3 2 1
#2 2 1
#1 1
#


n = int(input("Masukkan angka: "))
#contoh output n = 6
#720 6 5 4 3 2 1
#120 5 4 3 2 1
#24 4 3 2 1
#6 3 2 1
#2 2 1
#1 1
for i in range(n , 0, -1):
    hasil = 1
    for j in range(i, 0, -1):
        hasil = hasil * j
    print(hasil, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    