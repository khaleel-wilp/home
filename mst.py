import math
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(10)
root.left = Node(5)
root.left.right = Node(2)
root.right = Node(5)
root.right.right = Node(1)
root.right.right.left = Node(-1)

def min_sum(root):
    if root == None:
        return 0
    result = root.data
    leftresult = math.inf
    rightresult = math.inf
    if (root.left == None) and (root.right == None):
        return result
    else:
        if (root.left != None):
            leftresult = min_sum(root.left)
        if (root.right != None):
            rightresult = min_sum(root.right)
        if (leftresult < rightresult):
            result += leftresult
        else:
            result += rightresult
    return result

print (min_sum(root))

root = Node(7)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.left.left = Node(0)
root.right.left = Node(8)

print (min_sum(root))
