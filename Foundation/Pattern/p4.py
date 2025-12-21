'''
Pattern Printing
1

2 2 

3 3 3

4 4 4 4

5 5 5 5 5
'''


class pattern:
    def display(self, n):
        for i in range(0,n):
            for j in range(1,i+1):
                print(i, end=" ")
            print("\n")
p = pattern()
p.display(6)