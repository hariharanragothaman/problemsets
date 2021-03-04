from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        hmap = {}
        hmap = {k:v for k, v in sorted(ctr.items(), key= lambda item:item[1], reverse=True)}
        
        result = ""
        for k, v in hmap.items():
            result += k*v        
        return (result)
