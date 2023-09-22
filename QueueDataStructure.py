# Creating a class
class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def delete(self):
        try:
          return self.items.pop(0)
        except:
          print("Queue is empty")
    
    def display(self):
        for i in self.items:
          print(i)

#creating an object
my_queue = Queue()

# adding list of data to an object using for loop 
for i in range(1,6):
  my_queue.insert(i)

#display before deleting data from queue list
my_queue.display() #display number 1-5

#delete an item my list
my_queue.delete() #1 will be removed from the list
