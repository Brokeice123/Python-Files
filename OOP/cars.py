class car():
    def __init__(self, model, color, price, owner):
        self.model = model
        self.color = color
        self.price = price
        self.owner = owner


owner_1 = car("Toyota", "Silver", "Ksh 200,000", "Samuel")
print(owner_1.model)
print(owner_1.color)
print(owner_1.price)
print(owner_1.owner)
print("-----End of owner_1-----")

owner_2 = car("Alfa Romeo", "White", "Ksh 20,000,000", "Grace")
print(owner_2.model)
print(owner_2.color)
print(owner_2.price)
print(owner_2.owner)
print("-----End of owner_2-----")

owner_3 = car("Lotus", "Grey", "Ksh 30,200,000", "Daisy")
print(owner_3.model)
print(owner_3.color)
print(owner_3.price)
print(owner_3.owner)
print("-----End of owner_3-----")
