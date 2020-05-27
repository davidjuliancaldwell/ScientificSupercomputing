#!/usr/bin/python 

import random
import Node
import BinarySearchTree


tree = BinarySearchTree.BinarySearchTree()

for i in range(0,100):
    randomInt = random.randint(1,10000)
    tree.insert(randomInt)
    
tree.traverse()