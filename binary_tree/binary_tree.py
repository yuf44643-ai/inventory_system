#Node structure
class Node:           
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


#allocate memory for tree nodes
firstNode = Node("1(root)")
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)
fifthNode = Node(5)


#connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode 
secondNode.left = fourthNode
secondNode.right = fifthNode

#common Traversals method read all data under and include the node
#root -> left -> right
def preOrderTraversal(node):
    if node is None:
        return []
    return [node.data] + preOrderTraversal(node.left) + preOrderTraversal(node.right)

#left -> root -> right
def inOrderTraversal(node):
    if node is None:
        return []
    return inOrderTraversal(node.left) + [node.data] + inOrderTraversal(node.right)

#left -> right -> root
def postOrderTraversal(node):
    if node is None:
        return []
    return postOrderTraversal(node.left) + postOrderTraversal(node.right) + [node.data]

#Prints the elements of the traversal list separated by " > "
def printorder(Traversal):
    print(" > ".join(map(str, Traversal)))

printorder(preOrderTraversal(firstNode))
printorder(inOrderTraversal(firstNode))
printorder(postOrderTraversal(firstNode))
