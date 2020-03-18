from collections import Counter
class Solution:
    def min_window(self, s, t):
        # Classic 2 pointer strategy
        if not t or not s:
            return ""

        # This is to check the number of occurrences of characters in our interested string
        ctr = Counter(t)
        print(ctr)
        required = len(ctr)
        print(required)

        # Initiating the left and right pointers and others as needed
        left = right = 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None


        #ACTUAL LOGIC!

        while right < len(s):
            # Add one character from right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            # If the frequency of the current character added
            # equals to the desired count in 't' - ctr, increment formed by 1
            if character in ctr and window_counts[character] == ctr[character]:
                formed += 1
            # NOW WE HAVE TO TRY AND CONTRACT THE WINDOW, till the point it ceases to be desirable
            # Then try to expand?
            while left <= right and formed == required:
                character = s[l]

                # Save the smallest window
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)





        return "Hello World"


if __name__ == '__main__':
    s = "ABAACBAB"
    t = "ABC"

    # Expected answer is ACB
    s1 = Solution()
    result = s1.min_window(s, t)
    print(result)