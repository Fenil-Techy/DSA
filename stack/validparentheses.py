class Stack:
    def __init__(self):
        self.stack=[]
    def isValid(self,str):
        for ch in str:
            if ch in "([{":
                self.stack.append(ch)
                print(self.stack)
                
            else:
                if not self.stack:
                    return False
                
                top=self.stack.pop()

                if(ch==")" and top!="(") or \
                    (ch=="]" and top!="[") or \
                    (ch=="}" and top!="{"):
                        return False

        return len(self.stack)==0
            
        
str="{[()()]}"
        
s=Stack()
print(s.isValid(str))
            