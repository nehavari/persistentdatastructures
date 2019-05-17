def height(node):
    if not node:
        return 0
    left = 0
    right = 0
    if node.left:
        left = height(node.left)
    if node.right:
        right = height(node.right)

    if left > right:
        return left + 1
    else:
        return right + 1

def getBalanceFactor(node):
    return height(node.right) - height(node.left)

def isBalancedTree(root_node):
    if root_node:
        for node in root_node:
            balanceFactor = getBalanceFactor(node)
            if balanceFactor not in (-1, 0, 1):
                return False

    return True

