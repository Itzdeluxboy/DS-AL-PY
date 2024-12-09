class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    @staticmethod
    def parse_tuple(data):
        #to convert the tuple into a tree like structure

        if isinstance(data,tuple) and len(data)==3:
            node=TreeNode(data[1])
            node.left=TreeNode.parse_tuple(data[0])
            node.right=TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node

    


    def traverse_in_order(self):
        #helps in traversing the tree structure in order
        if self is None:
            return []
        return (self.left.traverse_in_order()+[self.key]+self.right.traverse_in_order())


    

    def tree_height(self):
        #finds the height of the tree
        if self is None:
            return 0
        return 1 +max(self.left.tree_height(), self.right.tree_height())

    def tree_size(self):
        #finds the size of the tree
        if self is None:
            return 0
        return 1 + self.left.tree_size()+self.right.tree_size()

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return ( self.left.to_tuple() if self.left else None,  self.key, self.right.to_tuple() if self.right else None)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())



def remove_none(nums):
    #removes None values from the tuple/list
    return [x for x in nums if x is not None]
def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and 
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))
    
    if not isinstance(node.key, (int, float, str)):
        raise ValueError("Tree keys must be numeric or strings for comparison.")


    min_key=min(remove_none([min_l, node.key, min_r]))
    max_key=max(remove_none([max_l,node.key,max_r]))

    return is_bst_node, min_key, max_key

tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
print(is_bst(tree1))
print(is_bst(tree2))