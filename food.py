import pet

class food:

    def __init__(self, suppliers, price, pet):
        self.suppliers = suppliers
        self.price = price
        self.pet = pet

f1 = food(suppliers="Royal Canin", price="1000", pet=[p1, p3])
f2 = food(suppliers="Perfect Fit", price="0", pet=[p1, p3])
f3 = food(suppliers="Chappi", price="0", pet=[p2, p4, p5])
f4 = food(suppliers="Purina One", price="2500", pet=[p2, p4, p5])