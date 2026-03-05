#Node structure
class Node:           
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


#allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)


#connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode 
secondNode.left = fourthNode

