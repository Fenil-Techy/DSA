class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def cycle(self):
        slow=self.head
        fast=self.head
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                print(True)
                return
        print(False)
    
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
# head.next.next.next.next.next=head
l=LinkedList(head)
l.cycle()


        