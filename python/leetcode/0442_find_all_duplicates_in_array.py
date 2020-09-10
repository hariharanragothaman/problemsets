import collections

nums = [4,3,2,7,8,2,3,1]
cnt = collections.Counter(nums)
print cnt

rst = [item for item, count in cnt.items() if count > 1]
print rst

