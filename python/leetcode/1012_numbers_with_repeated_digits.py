# To find number of postive integers with alteast 1 repeated digit within a given limit

import collections
import json

limit = 1962
sum = 0
for i in range(limit+1):
    ll = [ int(x) for x in str(i) ]
    cnt = collections.Counter(ll)
    count_json = json.dumps(cnt, sort_keys=True, indent=4)

    # parse dictionary
    count_dict = json.loads(count_json)
    for i in count_dict.values():
        if i > 1:
            sum += 1
print sum

