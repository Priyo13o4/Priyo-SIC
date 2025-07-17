class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SLLQueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, data):
        n = Node(data)
        if not self.rear:
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n
    def dequeue(self):
        if not self.front:
            return None
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val
    def display(self):
        t = self.front
        while t:
            print(t.data, end=' ')
            t = t.next
        print()

class DLLQueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, data):
        n = Node(data)
        if not self.rear:
            self.front = self.rear = n
        else:
            self.rear.next = n
            n.prev = self.rear
            self.rear = n
    def dequeue(self):
        if not self.front:
            return None
        val = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return val
    def display(self):
        t = self.front
        while t:
            print(t.data, end=' ')
            t = t.next
        print() 