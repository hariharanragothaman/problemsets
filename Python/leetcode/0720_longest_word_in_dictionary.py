class Solution:
    def longestWord(self, words: List[str]) -> str:
        sorted_words = sorted(words, reverse=True) 
        print("The sorted words is:", sorted_words)
        
        # Check if substrings are there:
        rlist = []
        
        for i, item in list(enumerate(sorted_words)):
            length = len(item)
        
            while length > 0:
                tmp = item[:length-1]
                if len(tmp) == 1:
                    rlist.append(item)               
                if tmp not in sorted_words:
                    break
                length = length -1
        print(rlist)
        
        gindex = 0
        for i in range(len(rlist)):
            if len(rlist[i]) > len(rlist[gindex]):
                gindex = i
            elif len(rlist[i]) == len(rlist[gindex]):
                if rlist[i] < rlist[gindex]:
                    gindex = i 
        
        return rlist[gindex]
