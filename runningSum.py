nums = [3,1,2,10,1]

#solution 1 with append
sum = []
sumLoop = 0
for i in nums:
    sumLoop += i
    sum.append(sumLoop)

print(sum)

#solution 2 with extednd
sum = []
sumLoop = 0
for i in nums:
    sumLoop += i
    sum.extend([sumLoop])
print(sum)

#solution 3 in place
for i in range(1, len(nums)):
    nums[i] += nums[i-1]
print(nums)
