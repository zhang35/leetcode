class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    curr = head
    prev = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def print_list(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    print_list(head)

    head = reverse_list(head)

    print("Reversed Linked List:", end="")
    print_list(head)