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

def pola_sakit_kepala(panjang, lebar):
    # Mengubah nilai panjang dan lebar menjadi positif
    panjang = abs(panjang)
    lebar = abs(lebar)
    
    # Memeriksa apakah panjang dan lebar adalah bilangan ganjil
    if lebar % 2 == 0 or panjang % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")
        return
    
    # Menghitung titik tengah untuk panjang dan lebar
    tengah_panjang = panjang // 2
    tengah_lebar = lebar // 2
    
    # Menghasilkan pola
    for i in range(panjang):
        for j in range(lebar):
            # Menghitung nilai dengan mengambil jarak terbesar dari pusat pola
            nilai = max(abs(tengah_panjang - i), abs(tengah_lebar - j)) + 1
            print(nilai, end=" ")
        print()

# Contoh penggunaan fungsi
pola_sakit_kepala(7,7)
