class Node:
  def __init__(self,value):
    self.value =value
    self.next =None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.leangth = 0
  
  def append(self,value):
    new_node = Node(value)
    if self.head is None:   
      self.head = new_node
      self.tail = new_node
    else:  
      self.tail.next = new_node
      self.tail = new_node
    self.leangth += 1
  
  def __str__(self):
    next_node = self.head
    result = ""
    while next_node is not None:
      result += str(next_node.value)
      if next_node.next is not None:
         result += " -> "
      next_node = next_node.next
    return result
  
  def prepend(self,value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.leangth += 1

  def insert(self,value,index):
    if self.leangth == 0:
      self.head = new_node
      self.tail = new_node

    if index == 0:
      self.prepend(value)
      return None
    
    if index == self.leangth:
       self.append(value)
       return None
    
    new_node = Node(value)
    pre_node = self.head 
    for i in range(self.leangth):
      if i == index - 1:
        new_node.next = pre_node.next
        pre_node.next = new_node
        self.leangth += 1
        return None
      pre_node = pre_node.next
    
  def traversal(self):
    current = self.head
    while current is not None:
      print(current.value)
      current = current.next
  
  def search(self,target):
    current = self.head
    while current is not None:
      if current.value == target:
        return True
      current = current.next
    return False
  
  def get(self,index):
    if index == -1:
      return self.tail
    if index < 0 or index > self.leangth:
      return "index not found"
    current = self.head
    for i in range(index):
      current = current.next
    return current
  
  def set_value(self,index,value):
    node = self.get(index)
    if node:
      node.value = value
      return True 
    return False
  
  def pop_first(self):
    if  self.leangth == 0:
      return 0
    
    if  self.leangth == 1:
      self.head = None 
      self.head = None
      self.leangth = 0
      return None
    
    heade_node = self.head
    self.head = self.head.next
    heade_node.next = None
    self.leangth -=1
    return None

  def pop(self):
    if  self.leangth == 0:
      return 0
      
    if  self.leangth == 1:
      self.head = None 
      self.head = None
      self.leangth = 0
      return None
    
    temp = self.head
    while temp.next is not self.tail: # tharget the second last node
      temp = temp.next
    temp.next = None
    self.tail = temp

  def remove(self,index):
    if index == 0:
      self.pop_first()
      return None
    
    if index >= self.leangth:
      return "indexs is not found"
    
    if index == self.leangth -1:
      self.pop()
      return None

    prev_node = self.get(index-1)
    remove_node = prev_node.next

    prev_node.next = remove_node.next
    remove_node.next = None
    self.leangth -=1

  def removeAll(self):
    self.head == None
    self.tail == None
    self.leangth = 0
 




  

new_linkedList = LinkedList()
print(new_linkedList)
print(new_linkedList.leangth)

# append first node 
new_linkedList.append(10)
print(new_linkedList.leangth)
print(new_linkedList.head.value)
print(new_linkedList.tail.value)

# append new node
new_linkedList.append(11)
print(new_linkedList.leangth)
print(new_linkedList.head.value)
print(new_linkedList.tail.value)

new_linkedList.append(12)
new_linkedList.append(13)
new_linkedList.prepend(9)
new_linkedList.prepend(7)
new_linkedList.insert(8,0)
print(new_linkedList)

print(new_linkedList.search(18))
print(new_linkedList.get(0))

print(new_linkedList.set_value(0,800))
print(new_linkedList)

new_linkedList.pop_first()
print(new_linkedList)

new_linkedList.pop()
print(new_linkedList)

new_linkedList.remove(5)
print(new_linkedList)

new_linkedList.remove(5)
print(new_linkedList)

new_linkedList.removeAll()
print(new_linkedList)

new_linkedList.append(000)
print(new_linkedList)







# new_linkedList.traversal()



 