class Circular:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        
    def enqueue(self,num):
        if(self.front==(self.rear+1)%self.size):
            print("queue is full")
            return
        if self.front==-1:
            self.front=0
        
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=num
    
    def dequeue(self):
        if(self.front==-1):
            print("queue is empty")
            return
        
        removed=self.queue[self.front]
        
        if(self.front==self.rear):
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return removed
    def display(self):
        if(self.front==-1):
            print("queue is empty")
            return
        
        i=self.front
        while True:
            print(self.queue[i],end=" ")
            if(i==self.rear):
                break
            i=(i+1)%self.size
        print()
            
q=Circular(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()

print(q.dequeue())
q.display()

q.enqueue(50)
q.enqueue(60)

q.display()