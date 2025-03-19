def int_to_str(angka):
    angka = str(angka)
    for i in angka:
        if i == '1':
            print('satu', end=' ')
        elif i == '2':
            print('dua', end=' ')
        elif i == '3':
            print('tiga', end=' ')
        elif i == '4':
            print('empat', end='')
        elif i == '5':
            print('lima', end=' ')
        elif i == '6':
            print('enam', end=' ')
        elif i == '7':
            print('tujuh', end=' ')
        elif i == '8':
            print('delapan', end=' ')
        elif i == '9':
            print('sembilan', end=' ')
        elif i == '0':
            print('nol', end=' ')
        
# Contoh Penggunaan
int_to_str(123)
# Output: satu dua tiga