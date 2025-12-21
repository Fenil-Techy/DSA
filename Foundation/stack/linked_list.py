class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    def __init__(self,head=None):
        self.head=head
    def push(self,data):
        add_node=Node(data)
        add_node.next=self.head
        self.head=add_node
    def pop(self):
        if self.head is None:
            return print("stack is empty")
        popped=self.head.data
        self.head=self.head.next
        return popped
    def peek(self):
        if self.head is None:
            return None
        return print(self.head.data)
    def isEmpty(self):
        return self.head is None
    
        

l=LinkedList()
l.push(10)
l.push(20)
l.push(30)
l.push(40)
l.pop()
l.pop()
l.pop()
l.pop()
l.peek()
print(l.isEmpty())


temp=l.head
while temp is not None:
    print(temp.data,end=" ")
    temp=temp.next