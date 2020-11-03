number = [-4, -1, -1, 0 ,1, 2]

def helper(first, middle, last):
    return first + middle+ last


ans = []
i = 0
first = number[i]

left = i + 1
right = len(number)-1
sum3 = helper(first, number[left], number[right])
print(i, left, right, sum3)

while left <= right:

    print(i, left, right)
    sum3 = helper(first, number[left], number[right])

    if sum3 == 0:
        ans.append([first, number[left], number[right]])
    elif sum3 < 0:
        left += 1
    elif sum3 > 0:
        right -= 1
    i += 1

print(ans)
