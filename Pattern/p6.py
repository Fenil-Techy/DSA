'''
Pattern Printing
     *      

    ***

   *****

  *******

 *********

***********
'''


class pattern:
    def display(self, n):
        for i in range(0,n):

            # left spaces
            for j in range(0, n-i-1):
                print(" ", end="")
            # stars
            for j in range(2*i + 1):
                print("*", end="")
            # right spaces
            for j in range(0,n-i- i):
                print(" ", end="")
            print("\n") 
p = pattern()
p.display(8)