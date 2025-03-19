batas_bawah = int(input("Masukkan batas bawah : "))
batas_atas = int(input("Masukkan batas atas : "))

def ganjil(batas_bawah,batas_atas):
    if batas_bawah < batas_atas:
        for i in range(batas_bawah,batas_atas):
            if i % 2 != 0:
                print(i) 
    elif batas_bawah > batas_atas:
        for n in range(batas_bawah, batas_atas, -1):
            if n % 2 != 0:
                print(n)
                
ganjil(batas_bawah,batas_atas)


