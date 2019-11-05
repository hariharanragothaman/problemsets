example_list = [6, 28, 496, 8128]
exmaple_tuple = [3.14, "pi", [True, False, True]]

"""
Similarities:
    Both represent sequences.
    Both use same syntax to access the ith element
    Both support 'in' operator for memebership checking

Differences:
    Tuple is IMMUTABLE
        -- You cannot change the element at index i, or add / delete from a tuple
           which is possible in a list
"""


class A():
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, A) and self.x == other.x

    def __hash__(self):
        """
        This is just the local hashing function here
        """
        return self.x *113 + 119



if __name__ == '__main__':
    u = A(42)






"""
Learnings:
    Tuples are used to hold heterogeneous groups of values.
    Lists are used for homogeneous group of values.
    Tuples are faster to build; and have a lesser memory footprint

    What are the actual benifits of immutability?
    1. Immutable objects are container friendly and thread-safe
    2. Example scenario: If an immutable object is inserted in a set
                         Changed
                         and then the changed object is looked up
                         --- the look up will fail!!

                    Since the hashcode has changed from when it was added into the set.
                    For this reason; tuples can be put into sets as map-keys, whereas lists cannot
"""
