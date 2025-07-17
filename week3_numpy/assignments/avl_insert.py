class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    update_height(node)
    balance = get_balance(node)
    # LL
    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    # RR
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    # LR
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # RL
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    return node

def preorder(node):
    if node:
        print(node.key, end=' ')
        preorder(node.left)
        preorder(node.right)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    root = None
    for x in arr:
        root = insert(root, x)
    preorder(root)
    print() 