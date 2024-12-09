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
    #helps in traversing the tree structure in order
    if node is None:
        return []
    return (traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right))


print(traverse_in_order(tree))

def tree_height(node):
    #finds the height of the tree
    if node is None:
        return 0
    return 1 +max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree))

def tree_size(node):
    #finds the size of the tree
    if node is None:
        return 0
    return 1 + tree_size(node.left)+tree_size(node.right)

print(tree_size(tree))



def remove_none(nums):
    return [x for x in nums if x is not None]
def is_bst(node):
    if node is None:
        return 0
    is_bst, min_l, max_l = is_bst(node.left)
    is_bst, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and 
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))
    
    min_key=min(remove_none([min_l, node.key, min_r]))
    max_key=max(remove_none([max_l,node.key,max_r]))

    return is_bst_node, min_key, max_key