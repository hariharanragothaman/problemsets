from collections import Counter


ll = ['abc', 'zef', 'abc', 'zef', 'def', 'lmn', 'kjl']

ctr = Counter(ll)
print(ctr.items())
res = sorted(ctr, key=lambda x: (-ctr[x], x))

print (res)
