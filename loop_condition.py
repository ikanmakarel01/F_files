# a = 1
# while a < 11:
#     print(a)
#     a += 1


# a = int(input("Masukkan angka: "))

# for i in range(0, a + 1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()



# while a < inputan:
#     a += 1
#     hasil = a
#     total_hasil = hasil 
#     print(total_hasil)
# hasil = 0
# n = int(input("Masukkan angka: "))
# for i in range(1, n + 1,1):
#     hasil += i

# print(hasil)

# n = 2
# a = 0

# for i in range(1,11):
#     hasil = n * i

# angka = [12,75,150,180,145,525,50]

# for i in angka:
#     if i > 500:
#         break
#     if i % 5 == 0:
#         if i > 150:
#             continue
#         print(i)

# a = int(input("Masukkan angka: "))
# for i in range(a + 1,0,-1):
#     for j in range(i-1,0,-1):
#         print(j, end=" ")
#     print()

# list1 = [1,2,3,4,5]
# a = len(list1) -1
# for i in range(a, -1, -1):
#     print(list1[i])

# for i in range(-10, 0, 1):
#     print(i)

# for i in range(5):
#     print(i)
# else:
#     print("Loop selesai")

# def cek_prima(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# for bilangan in range(25,51):
#     if cek_prima(bilangan):
#         print(bilangan)

# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num)

def fibonacci():
    angka = int(input("Masukkan angka: "))
    a, b = 0, 1
    for i in range(angka):
        print(a, end=' ')
        a, b = b, a + b
fibonacci()

def fibobonacci():
    angka = int(input("Masukkan angka: "))
    a, b = 0, 1
    count = 0

    while count < angka :
        print(a, end=' ')
        a, b = b, a + b
        count += 1
fibobonacci()

def fibonacci_kiri(n):
    fibo = [0, 1]  # Inisialisasi dua angka pertama
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])  # Tambah angka baru ke list
    return fibo[::-1]  # Balik urutan list

# Contoh penggunaan
n = int(input("Masukkan jumlah bilangan Fibonacci: "))
print("Bilangan Fibonacci Kiri:", fibonacci_kiri(n))



list_angka = [1, 2, 3, 4, 5]
terbesar = list_angka[0]

for angka in list_angka:
    if angka > terbesar:
        terbesar = angka

print("Angka terbesar adalah:", terbesar)


def fibonacci():
    angka = int(input("Masukkan angka: "))
    a, b = 0, 1
    deret = []  # List untuk menyimpan deret terbalik
    
    for _ in range(angka):
        deret.insert(0, str(a))  # Sisipkan di awal list
        a, b = b, a + b
    
    print(' '.join(deret))  # Gabungkan list jadi string

fibonacci()

def centered_average(nums):
    if len(nums) < 3:  # Pastikan ada cukup angka untuk dihitung
        raise ValueError("List harus memiliki minimal 3 angka")

    nums.sort()  # Urutkan list dari kecil ke besar
    trimmed_nums = nums[1:-1]  # Hapus nilai terkecil dan terbesar

    return sum(trimmed_nums) / len(trimmed_nums)