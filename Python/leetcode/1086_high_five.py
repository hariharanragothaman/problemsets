"""
Problem 1086: High Five

Given a list of scores of different students, return the average score of 
each student's top five scores in the order of each student's id.
Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.
The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 

Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores

"""

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

"""
# Sort dictionary by value; instead of key logic

dict1 = {}
for data in items:
    dict1[data[1]] = data[0]
return sorted(dict1.items(), key=lambda item: item[1])
"""

def highFive(items):
    result = []
    student_grades = {}

    grades = sorted(items, key=lambda x:x[1])
    print("Grades after sorting, based on grades\n", grades)

    ### - Groups items into a dictionary based on the given value in a "list"
    ### - CORE LOGIC
    """
    Going through the list, constructing the dictionary:-
    for this "key"; try to get the value? - If nothing is there []
                                            If it's there; add it to the list which is id_grades[1]
    """
  

    for id_grades in grades:
        student_grades[id_grades[0]] = student_grades.get(id_grades[0], []) + [id_grades[1]]
    print ("Converting List to Dictionary; and also grouping elements\n", student_grades)

    for key, value in student_grades.items():
        average = int(sum(value[-5:])/5)
        result.append([key, average])

    return sorted(result, key=lambda x:x[0])

result = highFive(items)
print("The result is: \n", result)

