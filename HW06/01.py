class BTree:

    class BTreeNode:
        __slots__ = ['element', 'parent', 'left', 'right']
        def __init__(self, element, parent = None, left = None, right = None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def search(self, key):
        x = self.root
        if x is None or x.element == key:
            return x
        while x is not None and x.element != key:
            if key < x.element:
                x = x.left
            else:
                x = x.right
        return x
    
    def minimum(self, x: BTreeNode):
        while x.left is not None:
            x = x.left
        return x
    
    def maximum(self, x: BTreeNode):
        while x.right is not None:
            x = x.right
        return x
    
    def successor(self, x: BTreeNode):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y
    
    def predecessor(self, x: BTreeNode):
        if x.left is not None:
            return self.maximum(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def insert(self, n: BTreeNode):
        y = None
        x = self.root

        while x is not None:
            y = x
            if n.element < x.element:
                x = x.left
            else:
                x = x.right
        n.parent = y
        if y is None:
            self.root = n
        elif n.element < y.element:
            y.left = n
        else:
            y.right = n

    def delete(self, n: BTreeNode):
        if n.left is None or n.right is None:
            y = n
        else:
            y = self.successor(n)
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != n:
            n.element = y.element
        return y

def tree_sum(node: BTree.BTreeNode):
    if not node:
        return 0
    return node.element + tree_sum(node.left) + tree_sum(node.right)

def tree_sum_iterative(node: BTree.BTreeNode):
    from collections import deque

    q = deque()
    q.append(node)

    sum = 0
    while q:
        curr = q.popleft()
        sum += curr.element
        if curr.left: 
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return sum

root = BTree()
root.insert(BTree.BTreeNode(5))
root.insert(BTree.BTreeNode(3))
root.insert(BTree.BTreeNode(2))
root.insert(BTree.BTreeNode(4))
root.insert(BTree.BTreeNode(7))
root.insert(BTree.BTreeNode(6))
root.insert(BTree.BTreeNode(8))

root_node = root.root
print(root.minimum(root_node).element)
print(root.maximum(root_node).element)
print(tree_sum_iterative(root_node))