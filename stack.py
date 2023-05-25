# Stack data structure could be described as stacking plates in your cubbard as you add to the top and remove from the top or the stack or first in first out. The oldest item in the stack would always be at the bottom and aways the last item to be removed. The newest item is the firt item to be removed.


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None


    def is_empty(self):
        if self.head == None:
            return True
        return False


    def size():
        pass


    def top(self):
        if self.is_empty():
            return None
        

    def push(self, data):
        if self.head == None:
            self.head = None(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node


    def pop(self):
        
        if self.is_empty():
            return None
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return  popped_node.data


