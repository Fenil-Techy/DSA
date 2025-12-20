class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None
        
    def isEmpty(self):
        return len(self.stack)==0

s=Stack()
s.push(10)
s.push(20)
print(s.peek())
s.pop()
print(s.peek())
print(s.isEmpty())

