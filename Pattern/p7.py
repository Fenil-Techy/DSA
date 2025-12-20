'''
*******

 *****

  ***

   *
'''

class pattern:
    def display(self, n):
        for i in range(0,n):

            # left spaces
            for j in range(0, i):
                print(" ", end="")
            # stars
            for j in range(0,2*(n-i)-1):
                print("*", end="")
            # right spaces
            for j in range(0,i):
                print(" ", end="")
            print("\n") 
p = pattern()
p.display(4)