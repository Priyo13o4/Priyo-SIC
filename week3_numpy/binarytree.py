class Node : 
    def __init__(self, data = 0):
        if data == 0:
            data = int(input('Enter data of the node: '))
        self.left = None
        self.data = data
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        print('An empty BST is created')

    def add_node(self):
        new_node = Node() # create a new Node object
        if self.root == None: # check if the tree is empty
            self.root = new_node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node
    
    def tree_height(self, node):
        if node is None:
            return -1
        return 1 + max(self.tree_height(node.left), self.tree_height(node.right))
        
class Menu:
    def __init__(self):
        self.choice = 0

    def is_tree_empty(self, bst):
        if bst.root == None:
            print('Tree is empty')
            return True
        return False

    def menu(self, bst):
        match self.choice:
            case 1 : bst.add_node()
        
            case 2 : 
                if self.is_tree_empty(bst):
                    return
                h = bst.tree_height(bst.root)
                print(f'Tree height is: {h}')
            case 3:
                self.choice = 0
            case _:
                print('Invalid choice')
    
    def start_app(self):
        bst = BST()
        while True:
            print('1:Add 2:Height 3:Exit')
            self.choice = int(input('Enter your choice: '))
            self.menu(bst)
            if self.choice == 0:
                print('Application closed')
                break
                
menu = Menu()
menu.start_app()