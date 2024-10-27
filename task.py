# Define a Queue class and implement the following methods: __init__, enqueue, dequeue, and is_empty. Specify the runtime of all methods except __init__.

# Bonus: How can we implement the queue so that all three runtimes are O(1)?
# answer by suelen: Implemente using a linked list or double linked list


class Queue:
   """A queue list"""

   queue = []

   
   def __init__(self):
      pass
   

   def enqueue(self):       #Time complexity of O(n)
      """Adding an item to the end of a Queue"""

      items = ["a", "b", "c"]

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
print(my_list.enqueue())
print(my_list.dequeue())
print(my_list.is_empty())



         



      
      




