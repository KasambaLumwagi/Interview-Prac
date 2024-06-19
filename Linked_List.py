class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

def length_of_linked_list(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
print(length_of_linked_list(head))
