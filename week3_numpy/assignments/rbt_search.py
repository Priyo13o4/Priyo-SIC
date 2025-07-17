class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(nodes):
    node_map = {}
    for val, l, r in nodes:
        if val not in node_map:
            node_map[val] = Node(val)
        node = node_map[val]
        if l != -1:
            if l not in node_map:
                node_map[l] = Node(l)
            node.left = node_map[l]
        if r != -1:
            if r not in node_map:
                node_map[r] = Node(r)
            node.right = node_map[r]
    return node_map[nodes[0][0]]

def search(node, key):
    if not node:
        return False
    if node.val == key:
        return True
    return search(node.left, key) or search(node.right, key)

if __name__ == "__main__":
    N = int(input())
    nodes = []
    for _ in range(N):
        vals = list(map(int, input().split()))
        nodes.append(vals)
    K = int(input())
    root = build_tree(nodes)
    print("Found" if search(root, K) else "Not Found") 