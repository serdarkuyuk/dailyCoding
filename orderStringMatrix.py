# matrix = [["c","b","a"],
#           ["d","a","f"],
#           ["g","h","i"]]

'''
matrix = ["a","b","c","d","e","f"]
matrix = [["z","y","x"],
          ["w","v","u"],
          ["t","s","r"]]


lengthCol = len(matrix[0])
lengthRow = len(matrix)

counter = 0
for j in range(lengthCol):
    for i in range(0,lengthRow-2):
         if ord(matrix[i][j]) > ord(matrix[i+1][j]):
             counter += 1
             continue
print(counter)
'''
# matrix = ["cba", "daf", "ghi"]
A =["xc","yb","za"]
# matrix =["ca","bb","ac"]
# lengthCol = len(matrix[0])
# lengthRow = len(matrix)
#
# counter = 0
# for j in range(lengthCol):
#     for i in range(0,lengthRow-1):
#         if ord(matrix[i][j]) < ord(matrix[i+1][j]):
#             pass# print(0)
#         else:
#             counter += 1
#             break
m, n = len(A), len(A[0])
ans, in_order = 0, [False] * (m-1)
for j in range(n):
    tmp_in_order = in_order[:]
    for i in range(m-1):
		# previous step, rows are not in order; and current step rows are not in order, remove this column
        if not in_order[i] and A[i][j] > A[i+1][j]: ans += 1; break
		# previous step, rows are not in order, but they are in order now
        elif A[i][j] < A[i+1][j] and not in_order[i]: tmp_in_order[i] = True
	# if column wasn't removed, update the row order information
    else: in_order = tmp_in_order
    # not necessary, but speed things up
    if all(in_order): print(ans)
print(ans)
# print(counter)
