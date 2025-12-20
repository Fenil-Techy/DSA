#simple pattern printing
class pattern1:
    def display(self, n):
        for i in range(0,n,1):
            for j in range(0,n,1):
                print("*", end=" ")
            print("\n")
p = pattern1()
p.display()