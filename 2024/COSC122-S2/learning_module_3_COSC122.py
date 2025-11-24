"""
LM 3 
TEST FILE
SEAN FAULKNER
12/09/2024
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

def print_linked_list(head):
    if head != None:
        print(head.data)
        next_node = head.next_node
        while next_node != None:
            print(next_node.data)
            next_node = next_node.next_node
            


head = Node(10)
head.next_node = Node(20)
head.next_node.next_node = Node(30)
head.next_node.next_node.next_node = Node(40)
print_linked_list(head)
print('Nothing to see here.')
head = None
print_linked_list(head)
print('Goodbye!')