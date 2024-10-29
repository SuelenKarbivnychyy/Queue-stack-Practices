# Define a Queue class and implement the following methods: __init__, enqueue, dequeue, and is_empty. Specify the runtime of all methods except __init__.

# Bonus: How can we implement the queue so that all three runtimes are O(1)?
# answer by suelen: Implemente using a linked list or double linked list


class Queue:
   """A queue list"""

   queue = []

   
   def __init__(self):
      pass
   

   def enqueue(self, items):       #Time complexity of O(n)
      """Add an item to the end of a Queue"""      

      for item in items:
        self.queue.append(item)

      return self.queue


   def dequeue(self):           #Time complexity of O(n)
      """Taking an item from the begining"""

      self.queue.pop(0)

      return self.queue


   def is_empty(self):    #Time complexity of O(1)
      """Check if the queue is empty"""
      
      return len(self.queue) == 0


my_list = Queue()
# print(my_list.enqueue(["a", "b", "c"]))
# print(my_list.dequeue())
# print(my_list.is_empty())



##################################################################

      
      
# Part 1: Define a class for a linked list node.

# Part 2: Write a function that takes in the head node of a linked list and prints the data of every node in the list.



class Node:
   """Node in a linked list."""

   def __init__(self, data):
      self.data = data
      self.next = None

   def __str__(self):
      return str(self.data)

   def __repr__(self):
      return f"<Node object. Data: {self}; Next: {self.next}>"
   



def print_nodes(head):
   """Print data of nodes"""

   current_node = head   
   
   while current_node:
      print(f" Current node: {current_node.data}, Next node: {current_node.next}")
      current_node = current_node.next



apple_node = Node("apple")
berry_node = Node("berry")
cherry_node = Node("cherry")
apple_node.next = berry_node
berry_node.next = cherry_node


print_nodes(apple_node)


