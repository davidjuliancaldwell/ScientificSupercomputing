#!/usr/bin/python

import linkedlist

L = linkedlist.LinkedList()
L.insert_at_head(1)
print("The value of the head is {0}".format(L.head.data))

L.insert_at_head(2)
print("The value of the head is now {0}".format(L.head.data))

L.insert_at_head(3)
print("The value of the head is now {0}".format(L.head.data))

a = L.delete_at_head()
print("The value at the head which was deleted was {0}".format(a))

L.insert_at_tail(40)
print("The value of the tail is now {0}".format(L.tail.data))

L.insert_at_tail(50)
print("The value of the tail is now {0}".format(L.tail.data))

L.insert_at_tail(60)
print("The value of the tail is now {0}".format(L.tail.data))
