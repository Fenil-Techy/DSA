'''
Pattern Printing
*

* *

* * *

* * * *

* * * * *
'''


class pattern:
    def display(self, n):
        for i in range(0,n):
            for j in range(0,i):
                print("*", end=" ")
            print("\n")
p = pattern()
p.display(6)