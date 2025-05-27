# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        new_node = Node(data)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)

# Input
# STDIN   Function
# -----   --------
# 4       T = 4
# 2       first data = 2
# 3
# 4
# 1       fourth data = 1


# Output
# Sample Output
# 2 3 4 1
