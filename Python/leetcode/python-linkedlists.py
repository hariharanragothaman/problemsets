class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def has_value(self, value):
        if self.val == value:
            return True
        else:
            return False

class SLL():
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = Listnode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def print_length(self):
        cnt = 0 
        curr_node = self.head
        while curr_node:
            cnt += 1
            curr_node = curr_node.next
        return cnt

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print curr_node.val
            curr_node = curr_node.next
        return

class Solution(object):
    def add_numbers(self, l1, l2):




if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)

    t1 = SLL()
    t1.add_list_item(n1)
    t1.add_list_item(n2)
    t1.add_list_item(n3)

    t1.print_list()
    length = t1.print_length()
    print "The length is:", length

    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)

