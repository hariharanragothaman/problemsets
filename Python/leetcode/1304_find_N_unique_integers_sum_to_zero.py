class Solution:
    def sumZero(self, n: int) -> List[int]:
        rlist = []    
        limit = 0 
        
        if n%2 != 0:
            limit = n//2+1
            rlist.append(0)            
            for i in range(1, limit):
                rlist.append(i)
                rlist.append(i*(-1))
        
        else:
            limit = n//2
            for i in range(1, limit+1):
                rlist.append(i)
                rlist.append(i*(-1))
        
           
        return rlist
