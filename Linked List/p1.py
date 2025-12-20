class Node():
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
class LinkedList:
    def __init__(self):
        self.head=None
    def Insert_head(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
l=LinkedList()
l.head=head
l.Insert_head(5)

temp=l.head
while temp is not None:
    print(temp.data,end=" ")
    temp=temp.next
