class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def insert(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    def display(self):
        t = self.head
        while t:
            print(t.data, end=' ')
            t = t.next
        print() 