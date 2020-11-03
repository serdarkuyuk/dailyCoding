A = ["cba",
     "daf",
     "ghi"]

lengthRow = len(A)
lengthCol = len(A[0])
result = 0
for col in range(lengthCol):
    for row in range(1, lengthRow):
        if (A[row][col] < A[row-1][col]):
            result += 1
            break
print(result)


ans = 0
for col in zip(*A):
    if any(col[i] > col[i+1] for i in range(len(col) - 1)):
        ans += 1
print(ans)
