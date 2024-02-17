# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement binary tree
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: binaryTree.py
#
# ------------------------------------------------------------

# Creating the binary tree class here
class BinaryTree:
    '''
    Creating the initialiser here
    '''
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    '''
    Creating the setting of key here
    '''
    def set_key(self, key):
        self.key = key

    '''
    Creating the getting of key here
    '''
    def get_key(self):
        return self.key
    
    '''
    Creating the getting the left here
    '''
    def get_left(self):
        return self.left
    
    '''
    Creating the getting the right here
    '''
    def get_right(self):
        return self.right

    '''
    Creating the insertion of left key here
    '''
    def insertLeft(self, key):

        # If left is none return the binary tree of it
        if self.left ==None:
            self.left = BinaryTree(key)
        
        # Else moving it to the left here
        else:
            tree = BinaryTree(key)
            self.left, tree.left = tree, self.left

    '''
    Creating the insertion of right key here
    '''
    def insertRight(self, key):

        # If right is none return the binary tree of it
        if self.right ==None:
            self.right = BinaryTree(key)
        
        # Else moving it to the right here
        else:
            tree = BinaryTree(key)
            self.right, tree.right = tree, self.right

    '''
    Creating the preorder function
    '''
    def printPreorder(self, level):

        # print the startng point here
        print( str(level*'-') + str(self.key))

        # if the left key is not none, print the left preorder with next level
        if self.left != None:
            self.left.printPreorder(level+1)
        
        # if the right key is not none, print the right preorder with next level
        if self.right != None:
            self.right.printPreorder(level+1)
    
    '''
    Creating the inorder function
    '''
    def printInorder(self, level):
    
        # if the right key is not none, print the right preorder with next level
        if self.right != None:
            self.right.printInorder(level + 1)

        # print the startng point here
        print(str(level * '.') + str(self.key))

        # if the left key is not none, print the left preorder with next level
        if self.left != None:
            self.left.printInorder(level + 1)

    '''
    Creating the postorder function
    '''
    def printPostorder(self, level):
        # if the left key is not none, print the left preorder with next level
        if self.left != None:
            self.left.printPostorder(level + 1)
        
        # if the right key is not none, print the right preorder with next level
        if self.right != None:
            self.right.printPostorder(level + 1)
        
        # print the startng point here
        print(str(level * '-') + str(self.key))

