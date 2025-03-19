def ganjil(bawah, atas):
    if bawah < atas:
        while bawah < atas:
            if bawah % 2 != 0:
                print(bawah)
            bawah = bawah + 1
    elif bawah > atas:
        while bawah > atas:
            if bawah % 2 != 0:
                print(bawah)
            bawah = bawah - 1

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
ganjil(bawah, atas)
