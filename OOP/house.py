class House():
    def __init__(self, type, location, owner):
        self.type = type
        self.location = location
        self.owner = owner


owner_one = House("Bungalow", "Kitengela", "Sharon")
print(owner_one.type)
print(owner_one.location)
print(owner_one.owner)

owner_2 = House("Mansion", "Syokimau", "Keith")
print(owner_2.type)
print(owner_2.location)
print(owner_2.owner)
