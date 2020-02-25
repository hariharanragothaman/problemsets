class Solution:
    def longestWord(self, words: List[str]) -> str:
        sorted_words = sorted(words, key=len, reverse=True)        
        print("The sorted words is:", sorted_words)
        
        # Check if substrings are there:
        rlist = []
        for i, item in list(enumerate(sorted_words)):
            length = len(item)            
            while length > 0:  
                if length == 1:
                    tmp = item
                else:
                    tmp = item[:length-1]
                  
                if tmp not in sorted_words:
                    break
                if len(tmp) == 1 and tmp in sorted_words and item not in rlist:
                    rlist.append(item)               
                length = length -1
        
        # Result 
        gindex = 0
        for i in range(len(rlist)):
            if len(rlist[i]) > len(rlist[gindex]):
                gindex = i
                
        max_length = len(rlist[gindex])      
        int_list = []
        for i in range(len(rlist)):
            if len(rlist[i]) == max_length:
                int_list.append(rlist[i])
                
        return(sorted(int_list)[0])
