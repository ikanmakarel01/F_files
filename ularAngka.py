def ularAngka(bawah, samping):
    for i in range(1, bawah + 1):
        if i % 2 == 1:
            for j in range(1, samping + 1):
                if j == 1 and i == 1:
                    print("head", end=" ")
                elif j == samping and i == bawah:
                    print("tail", end=" ")
                else:
                    angka = (i-1)*samping + j
                    if angka < 10:
                        print(f'0{angka}', end=" ")
                    else:
                        print(f'{angka}', end=" ")
        else:
            for j in range(samping, 0, -1):
                angka = (i-1)*samping + j
                if angka < 10:
                    print(f'0{angka}', end=" ")
                else:
                    print(f'{angka}', end=" ")
        print()

ularAngka(3, 4)
