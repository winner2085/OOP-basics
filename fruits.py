class Fruit:
    def __init__(self, name, color, taste, price):
        self.name = name
        self.color = color
        self.taste = taste
        self.price = float(price)
    
    #print fruit details
    def details(self):
        print(f"""
                *********************************
                Fruit Type: {self.name}
                Fruit Color: {self.color}
                Fruit Taste: {self.taste}
                Fruit Cost: {self.price}
                *********************************
            """)

    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            {self.name} Total Cost: {total}
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

apple = Fruit("Apple", "Green", "Sour", 1.25)
pear = Fruit("Pear", "Green", "Prickly sSweet", 5.45)
strawberry = Fruit("Strawberry", "Red", "Sweet", 2.30)
blueberry = Fruit("Blueberry", "Blue", "Sour", 2.50)
banana = Fruit("Banana", "Yellow", "Plain", 3.75)
orange = Fruit("Orange", "Orange", "Sweet", 2.50)

apple.details()
pear.details()
strawberry.details()
blueberry.details()
banana.details()
orange.details()

apple.calc_sales_tax(.04)
pear.calc_sales_tax(.04)
strawberry.calc_sales_tax(.04)
blueberry.calc_sales_tax(.04)
banana.calc_sales_tax(.04)
orange.calc_sales_tax(.04)