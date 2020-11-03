# g = [1,2,3]
# s = [3]

g = [10,9,8,7]
s = [5,6,7,8]

g.sort()
s.sort()

i = j = 0
satisfied = 0
while i < len(g) and j < len(s):
    if g[i] <= s[j]:
        satisfied += 1
        j += 1
        i += 1
    else:
        j += 1

print(satisfied)
