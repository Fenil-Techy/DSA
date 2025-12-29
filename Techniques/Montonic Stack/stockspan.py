class StockSpanner(object):
    def __init__(self):
        self.stack=[]
    def next(self,price):
        current_span=1
        while self.stack and self.stack[-1][0]<=price:
            index=self.stack.pop()
            current_span+=index[1]
        self.stack.append((price,current_span))
        return current_span

obj=StockSpanner()
prices = [30, 35, 40, 38, 35]

for price in prices:
    print(f"Price:{price}, Span:{obj.next(price)}")
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)