from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1 = Counter(words)        
        # This is the line of magic
        # print (dict1.items()) - This is a tuple
        # dict_items([('i', 2), ('love', 2), ('leetcode', 1), ('coding', 1)])
        """
        Thus, when awice is sorting by (-freq, word) in the heap, 
        this means that the heap prefers the tuples first with the highest frequency (most negative -freq) 
        and second alphabetically by the second field as Python compares strings alphabetically by default.
        
        """
        res = sorted(dict1, key=lambda x: (-dict1[x], x))
        return res[:k]
        
