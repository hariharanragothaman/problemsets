"""
1165: Single-Row Keyboard

@brief: Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25).
        Initially your finger is at index 0.
        To type a character, you have to move your finger to the index of the desired character.
        The time taken to move your finger from index i to index j is |i - j|.
        You want to type a string word. 
        Write a function to calculate how much time it takes to type it with one finger.
"""

def calculateTime(keyboard, word):
    cmp_dict = {}
    keyboard_list = [char for char in keyboard]
    for i, elements in list(enumerate(keyboard_list)):
        cmp_dict[elements] = i 
    word_list = [char for char in word]
    time_taken = 0
    prev_value = 0 
    for i, data in list(enumerate(word)):
        current_value = cmp_dict[data]
        time_taken += abs(current_value - prev_value)
        prev_value = current_value
    return time_taken

keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "leetcode"
result = calculateTime(keyboard, word)
print(result)
