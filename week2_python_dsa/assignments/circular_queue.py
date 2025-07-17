class CircularQueue:
    def __init__(self, size):
        self.q = [None]*size
        self.size = size
        self.front = self.rear = -1
    def enqueue(self, data):
        if (self.rear+1)%self.size == self.front:
            print('Full')
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear+1)%self.size
        self.q[self.rear] = data
    def dequeue(self):
        if self.front == -1:
            print('Empty')
            return
        val = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)%self.size
        return val
    def display(self):
        if self.front == -1:
            print('Empty')
            return
        i = self.front
        while True:
            print(self.q[i], end=' ')
            if i == self.rear:
                break
            i = (i+1)%self.size
        print() 