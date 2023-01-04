num = int(input("Enter number: "))
temporary = num
reverse = 0

while num != 0:
    rem = num % 10
    reverse = (reverse * 10) + rem
    num = num // 10

if temporary == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")