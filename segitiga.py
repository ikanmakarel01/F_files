# i = 1
# n = 5
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1

# a = 4
# for i in range(0, a + 1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# i = 5
# while i > 0:
#     j = 0
#     while j < i:
#         print("*", end="")
#         j += 1
#     print()
#     i = i - 1

a = 5
for i in range(a, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()