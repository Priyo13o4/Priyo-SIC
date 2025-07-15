class Node :
    def __init__(self,data):
        if data == 0 :
            data = int(input("please enter the data"))
        self.left = None
        self.data = data
        self.right = None

class BST :
    def __init__(self,root):
        self.root = None
        print("Any empty BST is created")
    def add_node(self) :
        new_node = Node()
        if self.root == None : 
            self.root = new_node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None :
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node