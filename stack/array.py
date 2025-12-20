class Stack:
    def __init__(self,cap):
        self.arr=[0]*cap
        
        self.capacity=cap
        self.top=-1
        
    def push(self,x):
        if self.top == self.capacity-1:
            print("stack overflow")
            return print(self.arr)
        self.top+=1
        self.arr[self.top]=x 
        return print(self.arr)
    def pop(self):
        if self.top==-1:
            print("stack is underflow")
            return -1
        value=self.arr[self.top]
        self.arr[self.top]=0
        self.top-=1
        print(value)
        print(self.arr)
    
s=Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.pop()

