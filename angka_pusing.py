def pola_sakit_kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)
    
    if lebar % 2 == 0 or panjang % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")
        return
    
    tengah_panjang = panjang // 2
    tengah_lebar = lebar // 2
    
    for i in range(panjang):
        for j in range(lebar):
            nilai = abs(tengah_panjang - i) + abs(tengah_lebar - j) + 1
            print(nilai, end=" ")
        print()


pola_sakit_kepala(7, 7)
