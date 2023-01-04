def Reverse(str):
    reversedString = str[::-1]
    return reversedString

originalString = input("Enter string: ")

outputString = Reverse(originalString)

if originalString == outputString:
    print("This string is a pallindrome")
else:
    print("This string is not a pallindrome")