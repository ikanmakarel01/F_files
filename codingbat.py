bilangan1 = input("masukkan bilangan 1: ")
bilangan2 = input("masukkan bilangan 2: ")

try:
    bilangan1 = int(bilangan1)
    bilangan2 = int(bilangan2)
    if bilangan1 > bilangan2:
       print("bilangan 1 lebih besar dari bilangan 2")
    else:
       print("bilangan 2 lebih besar dari bilangan 1")
except:
    print("input harus berupa angka")






