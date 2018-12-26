
class Holding(object): 
    '''
    A collection of functions and the functions actually serve as methods
    one access through the . operation.
    '''

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self): #define a cost method that carries out calculation
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


# h = Holding('AA', '2012-12-26', 100, 34)
# h.name
# h.date
# h.shares
# h.cost()
# h.sell(10)
# h.shares