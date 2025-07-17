class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLLStack:
    def __init__(self):
        self.top = None
    def push(self, data):
        n = Node(data)
        n.next = self.top
        self.top = n
    def pop(self):
        if not self.top:
            return None
        val = self.top.data
        self.top = self.top.next
        return val
    def display(self):
        t = self.top
        while t:
            print(t.data, end=' ')
            t = t.next
        print() 