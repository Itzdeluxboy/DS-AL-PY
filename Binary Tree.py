class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
# node0 = TreeNode(3)
# node1 = TreeNode(4)
# node2 = TreeNode(5)


# print(node0.key, node1.key, node2.key)
        
tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    #to convert the tuple into a tree like structure

    if isinstance(data,tuple) and len(data)==3:
        node=TreeNode(data[1])
        node.left=parse_tuple(data[0])
        node.right=parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree= parse_tuple(tree_tuple)


def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right))


print(traverse_in_order(tree))

def tree_height(node):
    if node is None:
        return 0
    return 1 +max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left)+tree_size(node.right)

print(tree_size(tree))