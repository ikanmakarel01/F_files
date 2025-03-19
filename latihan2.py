a = int(input("Masukkan bilangan a: "))
b = int(input("Masukkan bilangan b: "))
c = int(input("Masukkan bilangan c: "))

d = (b**2) - (4*a*c)

if d >= 0:
    print("Akar real/Nyata")
elif d > 0:
    print("Akar real dan berlainan")
elif d == 0:
    print("Akar real dan kembar")
else:
    print("Akar imajiner/Tidak Real/Khayal")
    
