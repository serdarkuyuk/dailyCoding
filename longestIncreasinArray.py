arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
     #[1, 2, 2, 3,  2,  3, 3,  4, 2, 3, 3, 4,  3, 4,  4, 5]
# arr = [-1, 3, 4, 5, 2, 2, 2, 2]

result = [1] * len(arr)

for j in range(1, len(arr)):
    for i in range(0, j):
        if arr[j] > arr[i]:
            result[j]  = max(result[j], result[i]+1)
print(result)


#nlogn solution
from bisect import bisect_left

if not nums:
    return 0


result = []

for num in nums:
    if not result or num > result[-1]:
        result.append(num)
    else:
        index = bisect_left(result, num)
        result[index] = num

return len(result)
