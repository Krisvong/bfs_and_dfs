# imports the deque class from the collections module
from collections import deque

# define a class 'Node', which represents a node in the binary tree.  The 'Node' class has attributes 'data', 'left', and 'right to store the node's value, and references to its left and right children
class Node:     # TreeNode
  # In the __init__ method, it initializes the attributes based on the provided 'key'. If the 'key' is "null", it sets 'data' to 'None', indicating an empty node. Otherwise, it sets 'data' to the provided 'key'.
  def __init__(self, key):
    if key == "null":
      self.data = None
    else:
      self.data = key
    self.left = None
    self.right = None

# define a function that calculates the maximum value in each level of the binary tree using a breadth-first traversal approach. It will take the root node of the binary tree as input
def levelMax(root):
  Q = deque() # used as a queue to perform the breadth-first traversal. It stores the nodes to be visited in a level
  V = [] # list used to track visited nodes
  M = set() # set used to keep track of visited nodes to avoid revisiting them
  bigs = [] # list that will store the maximum value in each level

  Q.appendleft(root) # the root is added to the queue ('Q') to start the traversal

  while len(Q) != 0: # the traversal contintues while the queue ('Q') is not empty
    big = 0 # for each level, a new 'big' variable is initialized to track the maximum value in that level
    for _ in range(len(Q)): # the inner loop iterates over the nodes in the current level
      cur = Q.pop() # the current node is removed from the queue ('Q.pop()') and its value is compared to 'big' to update the maximum value if necessary
      V.append(cur)
      if cur.data > big:
        big = cur.data
      # for each child node (left and right), if the child has not been visited('child not in M') and its not 'None', it is added to the queue ('Q.appendleft(child)') and marked as visited ('M.add(child)')
      for child in [cur.left, cur.right]:
        if child not in M and child is not None:
          Q.appendleft(child)
          M.add(child)
    # after processing all nodes in the current level, the maximum value ('big') is added to the 'bigs'list      
    bigs.append(big)  
  return bigs 


# entry point of the code. Define a function that takes the input array 'lst' as a parameter, which represents the binary tree
def max_levels(lst):
  # intialize a variable 'levels' to 0, which will store the number of levels in the binary tree
  levels = 0
  # iterate from 0 to 9(assuming a maximum of 10 levels for the tree)
  for i in range(10):
    # if the length of the input array 'lst' matches the formula '2**i - i', where i is the current loop variable 
    if len(lst) == 2**i - 1:
      # if the condition in met, it means the number of nodes in the tree matches the formula, and 'levels' is set to 'i + 1' to account for 0-indexing. 
      levels = i + 1
      # The loop is then broken
      break


  # Create a binary tree using the 'Node' class
    root = Node(lst[0])  # Create the root node with the value from lst[0]

    root.left = Node(lst[1])  # Create the left child node of the root with the value from lst[1]
    root.right = Node(lst[2])  # Create the right child node of the root with the value from lst[2]

    root.left.left = Node(lst[3])  # Create the left child node of the left child of the root with the value from lst[3]
    root.left.right = Node(lst[4])  # Create the right child node of the left child of the root with the value from lst[4]

    root.right.right = Node(lst[6])  # Create the right child node of the right child of the root with the value from lst[6]


    print(levelMax(root))

max_levels([5, 3, 8, 2, 4, 'null', 9])
