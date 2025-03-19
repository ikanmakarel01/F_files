#Buatlah program untuk mencari bilangan prima terdekat dari suatu bilangan
#Yang di input oleh user (n). dan nilai bilangan prima tersebut < n
#Contoh:input n = 12, maka outputnya adalah 11

n = int(input("Masukkan angka: "))
n_asli = n
count = 1
while count < 2:
    n = n - 1
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print (f"Bilangan prima terdekat < {n_asli} adalah {n}")
        count += 1


# def prima_dekat(n):
#     if n <= 2:
#         return "Tidak ada bilangan prima dekat"
#     else:
#         for i in range(n-1, 1, -1):
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 print(i, end=" ")
#                 break