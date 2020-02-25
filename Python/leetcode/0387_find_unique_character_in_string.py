class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1   
        
        s_list = [c for c in s]
        hashmap = {}
        
        for i, data in list(enumerate(s_list)):
            if data not in hashmap:
                hashmap[data] = [i]
            else:
                hashmap[data].append(i)
                
        rlist = []       
        for key, value in hashmap.items():
            if len(value) == 1:
                rlist.append(value)
        
        if not rlist:
            return -1
        else:
            ll = sorted(rlist)
            return ll[0][0]
