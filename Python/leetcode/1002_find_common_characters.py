"""
Problem 1002: Find common characters
"""
def commonCharacters(input_list):
    """
    We are implicitly the input_list implicitly; 
    So that's why the loop looks so simple!!
    LOGIC:

    1. Keep the first-string in the list as the seed value.
    2. The loop is going to continue till the first word in the list length is greater than zero.
    3. Now, if a character in the first-string is not there in other words, remove it from the first-string.
    4. If it's there in other words, remove it "once" from all other words.
    """
    
    results = []
    # Common characters in all strings within the list
    # hence - considering the first one as an seed / example!
    while len(input_list[0]) > 0:
        print("*******************")
        print("The input_list now is:", input_list)
        # If the char is in every other word in the list
        if all(input_list[0][0] in data for data in input_list):
            print("Match found: The input_list now is:", input_list)
            results.append(input_list[0][0])
            input_list = [data.replace(input_list[0][0], '', 1) for data in input_list]
        else:
            print("???!!!: The input_list now is:", input_list)
            input_list[0] = input_list[0].replace(input_list[0][0], '', 1)
    return results

input_list = ["bella", "label", "roller"] 
res = commonCharacters(input_list)
print(res)
