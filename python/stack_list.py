class Stack:
    def __init__(self):
          self.stack = []
    def push(self,item):
         self.stack.append(item)

    def pop(self):
         if not self.is_empty():
              return self.stack.pop()
         return None

    def is_empty(self):
         return len(self.stack) ==0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)
   
s= Stack()
s.push(2)
s.push(7)
print(s.pop())
print(s.pop())
print(s.pop())
    
          