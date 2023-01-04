arr =[]

capacity = int(input("Enter capacity of array: "))

for i in range(capacity):
    arr.append(int(input("Enter " + str(i) + " value: ")))

print(arr)

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

