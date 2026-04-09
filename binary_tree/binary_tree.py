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

#simple binary tree created
#        1
#       / \
#      2   3
#     / \
#    4   5

#common Traversal methods
#Depth-First Traversal
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

#Breadth-First Traversal
def levelOrderTraversal(node):
    if node is None:
        return []
    #using queue (first in first out)
    result = []
    queue = [node]
    while len(queue) > 0:
        current_node = queue.pop(0)
        result.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return result

#Prints the elements of the traversal list separated by " > "
def printorder(Traversal):
    print(" > ".join(map(str, Traversal)))

printorder(preOrderTraversal(firstNode))
printorder(inOrderTraversal(firstNode))
printorder(postOrderTraversal(firstNode))
printorder(levelOrderTraversal(firstNode))

