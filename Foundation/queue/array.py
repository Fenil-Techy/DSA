class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,num):
        self.queue.append(num)
        return self.queue
    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
            return
        self.queue.pop(0)
        return self.queue
    def front(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue[0]
        
q=Queue()
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.front())
print(q.dequeue())
# print(q.front())