class Solution:   
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(0, len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False            
            t = t[index+1:]
        return True

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """
        1. The first step is to sort the word in descending order of their length
        
        """
        d = sorted(d, key=len, reverse=True)
        hashmap = {}
        for word in d:
            res = self.isSubsequence(word,s)
            if res:
                length = len(word)
                hashmap[word] = length
                
        if not hashmap:
            return ""
        
        hashmap = {k:v for k, v in sorted(hashmap.items(), key= lambda item:item[1], reverse=True)}
        max_length = (list(hashmap.values())[0])
        
        rlist = []   
        for k, v in hashmap.items():
            if v == max_length:
                rlist.append(k)
            else:
                break
                
        rlist = sorted(rlist)
        return rlist[0]
