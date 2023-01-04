
n = int(input("Enter height of pyramid: "))

for i in range(0, n):

    for j in range(0, i + 1):
        print("* ", end="")

    print("\r")
