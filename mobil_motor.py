jenis_kendaraan = input("Jenis Kendaraan: ")
waktu_parkir = int(input("Waktu Parkir: "))
biaya_motor = 0
biaya_mobil = 0


if jenis_kendaraan == "motor":
    if waktu_parkir <= 2:
        biaya_motor = 2000
    elif waktu_parkir > 24:
        biaya_motor = 15000 + (15000 * 0.5)
    elif waktu_parkir >= 3:
        biaya_motor = 2000 + (waktu_parkir - 2) * 1000
        if biaya_motor > 15000:
            biaya_motor = 15000
    print("Biaya Parkir Motor: ", biaya_motor)

if jenis_kendaraan == "mobil":
    if waktu_parkir <= 1:
        biaya_mobil = 5000
    elif waktu_parkir > 24:
        biaya_mobil = 65000 + (65000 * 0.5)
    elif waktu_parkir >= 2:
        biaya_mobil = 5000 +(waktu_parkir - 1) * 3000
        if biaya_mobil > 65000:
            biaya_mobil = 65000
    print("Biaya Parkir Mobil: ", biaya_mobil)