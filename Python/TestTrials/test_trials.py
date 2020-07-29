class Solution:
    def getsteps(self, n):
        steps = 0
        while n != 1:
            print("The value of n:", n)
            if n % 2 == 0:
                n = n / 2
                steps += 1
            if n % 2 != 0:
                n = (3 * n) + 1
                steps += 1
        return steps

    def getKth(self, lo: int, hi: int, k: int) -> int:
        hashmap = {}
        while lo < hi:
            print("the val is", lo)
            res = self.getsteps(lo)
            print("res is:", res)
            hashmap[lo] = res
            lo += 1

        print(hashmap)


s = Solution()
s.getKth(12,15,2)