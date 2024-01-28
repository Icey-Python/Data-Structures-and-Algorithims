#question one:
#Remove duplicates from array

nums:list =[1,2,3,5,8,6,54,197,3,81,3,91,6,6,3,98,2,9,2,6]

for i in nums:
    times_appeared = 0
    for idx,k in enumerate(nums):
        if k == i and times_appeared<1:
            times_appeared +=1

    print(f"times appeared for: {i} is {times_appeared}")
print(nums)
