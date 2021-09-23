#!/usr/bin/env python3
"""
`trees` implementation and driver
Turning in-order and post-order tree traversals into pre-order


@authors: Roman Yasinovskyy
@version: 2021.9
"""
class Trees:
    def __init__(self, val, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val


def get_preorder(inorder: str, postorder: str) -> str:
    """
    Returns pre-order traversal of a tree based on its in-order and post-order traversals

    :param inorder: in-order tree traversal
    :param postorder: post-order tree traversal
    :return: pre-order tree traversal
    >>> get_preorder("UOMELBARTKGSNI", "UMELABORSGNIKT")
    'TROUBLEMAKINGS'
    """
    # TODO: Implement this function
    inorder = list(inorder)
    postorder = list(postorder)
    def recFunction(inorder, postorder):
        if not inorder or not postorder:
            return
        # pop the last element of postorder to get the root Node
        root = Trees(postorder.pop())
        mid = inorder.index(root.val)
        root.right = recFunction(inorder[mid+1:], postorder)
        root.left = recFunction(inorder[:mid], postorder)
        return root
    rootNode =  recFunction(inorder, postorder)
    return preorder(rootNode)

def preorder(rootNode):
    def convertToString(rootNode, string):
        if rootNode == None or rootNode.val == 0:
            return 
        if rootNode.left == None and rootNode.right == None:
            return str(rootNode.val)
        finalFormation = str(rootNode.val)
        # recursive call to the left
        if rootNode.left != None:
            finalFormation += convertToString(rootNode.left, '')
        else:
            finalFormation = finalFormation
        # Recursive call to the right
        if rootNode.right != None:
            finalFormation += convertToString(rootNode.right, '')
        return finalFormation
    return convertToString(rootNode, '')
    





def main():
    """This is the main function"""
    print("Pre-order tree traversal")
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()
