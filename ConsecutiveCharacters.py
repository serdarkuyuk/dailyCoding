# s = "abbcccddddeeeeedcba"
# s = "tourist"
s = "leetcode"
count = 1
maxcount = i = 0
previous = None
while i < len(s):
    if s[i] == previous:
        count += 1
    else:
        count = 1
        previous = s[i]
    i += 1
    maxcount = max(maxcount, count)
print(maxcount)

'''s = "tourist"
mylist = [1]
i = 1
while i < len(s):
    mylist.append(1)
    print(s[i],s[i-1])
    if s[i] == s[i-1]:
        mylist[i] = max(mylist[i], mylist[i-1]+1)
        print(mylist)
    i += 1
    print(i)
print(max(mylist))'''
