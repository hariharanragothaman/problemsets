"""
Problem 1002: Find common characters
"""
def commonCharacters(input_list):
    """
    We are implicitly the input_list implicitly; 
    So that's why the loop looks so simple!!
    """
    
    results = []
    # Common characters in all strings within the list
    # hence - considering the first one as an seed / example!
    while len(input_list[0]) > 0:
        # If the char is in every other word in the list
        if all(input_list[0][0] in data for data in input_list):
            results.append(input_list[0][0])
            input_list = [data.replace(input_list[0][0], '', 1) for data in input_list]
        else:
            input_list[0] = input_list[0].replace(input_list[0][0], '', 1)
    return results

input_list = ["bella", "label", "roller"] 
res = commonCharacters(input_list)
print(res)
