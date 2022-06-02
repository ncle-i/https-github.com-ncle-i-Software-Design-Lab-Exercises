import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def thesecondlastnode(head):
    temp = head

    if (temp == None or temp.next == None):
        return -1

# Traverse the linked list
    while (temp != None):

        if (temp.next.next == None):
            return temp.data

        temp = temp.next


def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head



if __name__ == '__main__':
    head = None

    head = push(head, 172)
    head = push(head, 15)
    head = push(head, 79)
    head = push(head, 41)
    head = push(head, 24)

    print(thesecondlastnode(head))