'''
Pattern Printing
1

1 2

1 2 3

1 2 3 4

1 2 3 4 5
'''


class pattern:
    def display(self, n):
        for i in range(0,n):
            for j in range(1,i+1):
                print(j, end=" ")
            print("\n")
p = pattern()
p.display(6)