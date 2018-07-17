"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
     self.head = None
     self.tail = None

  def add_to_tail(self, value):
      node = Node(value)
    if self.head == None:
      self.head = node
    elif self.head == self.tail and self.head != None:
      self.head.set_next(node)
    else:
      self.tail.set_next(node)
    self.tail = new_node

  def remove_head(self):
    if self.head is not None:
      removed_head = self.head

    if removed_head.next_node is not None:
        self.head = removed_head.next_node
    else:
        self.head = None
    return removed_head.value

  def contains(self, value):
    pass

  def get_max(self):
    pass
