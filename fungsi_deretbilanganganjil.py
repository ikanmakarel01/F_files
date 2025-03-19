# .2 Buatlah program yang dapat menampilkan deret bilangan ganjil dari batas bawah
# dan batas atas yang diberikan oleh pengguna. Jika ternyata batas atas < batas bawah, berarti
# deret tersebut dimulai dari batas atas, sampai batas bawah (negatif range). Buatlah fungsi ganjil()
# dalam program tersebut! Berikut ini adalah contoh hasil yang diharapkan:
# • bawah = 10, atas = 30. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya
# adalah: 11, 13, 15, 17, 19, 21, 23, 25, 27, 29.
# • bawah = 97, atas = 82. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya
# adalah: 97, 95, 93, 91, 89, 87, 85, 83.


# def ganjil(bawah, atas):
#     if bawah > atas:
#         langkah = -1  # Untuk iterasi mundur jika bawah > atas
#     else:
#         langkah = 1  # Untuk iterasi maju jika bawah <= atas
    
#     # Menyesuaikan batas bawah jika bukan ganjil
#     if bawah % 2 == 0:
#         bawah += langkah
    
#     for i in range(bawah, atas + langkah, 2 * langkah):
#         print(i, end=" ")
#     print()

# # Input dari pengguna
# bawah = int(input("Masukkan batas bawah: "))
# atas = int(input("Masukkan batas atas: "))
# ganjil(bawah, atas)

def ganjil(bawah, atas):
    if bawah <= atas:
        urutan = 2 # Iterasi maju
    else:
        urutan = -2  # Iterasi mundur

    if bawah % 2 == 0:
        if urutan > 0:
            bawah = bawah + 1  # Tambah 1 jika iterasi maju
        else:
            bawah = bawah - 1  # Kurangi 1 jika iterasi mundur

    # Iterasi menggunakan range dengan step yang sesuai
    if urutan > 0:
        batas_akhir = atas + 1  # Jika iterasi maju, tambahkan 1 pada batas akhir
    else:
        batas_akhir = atas - 1  # Jika iterasi mundur, kurangi 1 pada batas akhir

    for i in range(bawah, batas_akhir, urutan):
        print(i, end=" ")
    print()

# Input dari pengguna
bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

ganjil(bawah, atas)

