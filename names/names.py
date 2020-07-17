import time
import math
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# BST
# root = None
# for name in names_1:
#   if root is None:
#     root = BSTNode(name)
#   else:
#     root.insert(name)

# for name in names_2:
#   if root.contains(name):
#     duplicates.append(name)

# STRETCH
names_1.sort()

def binary_search(names, search_value):
  left = 0
  right = len(names) - 1
  while left <= right:
    mid = math.floor((left + right) / 2)
    if names[mid] < search_value:
      left = mid + 1
    elif names[mid] > search_value:
      right = mid - 1
    else:
      return True
  return False

for name in names_2:
  if binary_search(names_1, name):
    duplicates.append(name)

# set (to see best time)
# names_1_set = set(names_1)
# names_2_set = set(names_2)
# duplicates = names_1_set.intersection(names_2_set)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
