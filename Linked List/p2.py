class Node():
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def Insert_end(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
l=LinkedList(head)
l.Insert_end(5)

temp=l.head
while temp is not None:
    print(temp.data,end=" ")
    temp=temp.next
print("None")

