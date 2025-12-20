class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self,front=None):
        self.front=front
        self.rear=None
        
    def enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.rear=self.front=new_node
            return
        self.rear.next=new_node
        self.rear=new_node
        
    def dequeue(self):
        if self.front is None:
            self.rear=None
            print("Queue is empty")
            return
        self.front=self.front.next
        return
    
    def peek(self):
        if self.front is None:
            self.rear=None
            print("Queue is empty")
            return
        return self.front.data
    
    def display(self):
        temp=self.front
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        return
            
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q.display())
print(q.peek())

q.dequeue()
print(q.display())
print(q.peek())

        
            