"""
Problem: 771: Jewels and Stones

@brief: You're given strings J representing the types of stones that are jewels, and S representing the stones. 
        Each character in S is a type of stone you have.  
        You want to know how many of the stones you have are also jewels.

        The letters in J are guaranteed distinct, and all characters in J and S are letters.
        Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
def numJewelsInStones(self, J: str, S: str) -> int:
    """
    Python one-liner for this is:
    return sum(S.count(j) for j in J)
    """

    J_list = [char for char in J]
    S_list = [char for char in S]
    count = 0 
    for element in S_list:
        if element in J_list:
            count +=1
    return count
