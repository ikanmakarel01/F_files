def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for bilangan in range(25,51):
    if cek_prima(bilangan):
        print(bilangan)