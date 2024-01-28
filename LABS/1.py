import random
def summation(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def maximum(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

n = int(input("Enter the length of the array: "))
array = []

for i in range(n):
    num = random.randint(0,n)
    array.append(num)
print(array)

sum = summation(array)
print("The sum of the array is:", sum)  

max = maximum(array)
print("The maximum value in the array is:", max)
