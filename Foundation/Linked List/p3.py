class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,head=None):
        self.head=head
        
    def insert(self,data,pos):
        add_node=Node(data)
        
        if pos==0:
            add_node.next=self.head
            self.head=add_node
            return
        
        temp=self.head
        count=0
        while temp is not None and count<pos-1:
            temp=temp.next
            count+=1
        if temp is not None:
            add_node.next=temp.next
            temp.next=add_node
    def delete(self,pos):
        
        if self.head is None:
            return
        
        if pos==0:
            self.head=self.head.next
            return
        
        temp=self.head
        count=0
        while temp is not None and count<pos-1:
            temp=temp.next
            count+=1
        if temp is not None and temp.next is not None:
            temp.next=temp.next.next
            
    def reverse(self):
        prev=None
        temp=self.head
        while temp is not None:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        
        self.head=prev
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
       
l=LinkedList(head)
l.reverse()
temp=l.head
while temp is not None:
    print(temp.data,end=" ")
    temp = temp.next
