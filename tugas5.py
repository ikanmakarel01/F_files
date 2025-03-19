# Input
gaji_per_jam = float(input("Masukkan gaji per jam: "))
jumlah_jam_kerja = int(input("Masukkan jumlah jam kerja dalam seminggu: "))

# Perhitungan
pendapatan_sebelum_pajak = gaji_per_jam * jumlah_jam_kerja * 5
pajak = pendapatan_sebelum_pajak * 0.14
pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak
biaya_pakaian_aksesoris = pendapatan_setelah_pajak * 0.10
biaya_alat_tulis = pendapatan_setelah_pajak * 0.01
sisa_uang = pendapatan_setelah_pajak - biaya_pakaian_aksesoris - biaya_alat_tulis
sedekah = sisa_uang * 0.25
dana_anak_yatim = sedekah * 0.3
dana_kaum_dhuafa = sedekah * 0.7

# Output
print("Pendapatan Budi sebelum pajak:", pendapatan_sebelum_pajak)
print("Pendapatan Budi setelah pajak:", pendapatan_setelah_pajak)
print("Biaya pakaian dan aksesoris:", biaya_pakaian_aksesoris)
print("Biaya alat tulis:", biaya_alat_tulis)
print("Jumlah sedekah Budi: Rp ", sedekah)
print("Dana anak yatim:", dana_anak_yatim)
print("Dana kaum dhuafa:", dana_kaum_dhuafa)