'''
Pattern Printing
* * * * * * 

* * * * *

* * * *

* * *

* *

*
'''


class pattern:
    def display(self, n):
        for i in range(0,n):
            for j in range(1,n-i):
                print(j, end=" ")
            print("\n")
p = pattern()
p.display(6)