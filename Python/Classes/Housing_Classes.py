class Habitat:
    def __init__(self):
        self.bedrooms = None
        self.bathrooms = None
        self.floors  = None
    def setHabitat(self):
        self.bedrooms = input("How many bedrooms:")
        self.bathrooms = input("How many bathrooms:")
        self.floors = input("How many floors is your habitat:")
class House(Habitat):
    def __init__(self):
        Habitat.__init__(self)
        self.garage = None
        self.taxes = None
        self.price = None
    def setHouse(self):
        self.garage = input("Does the house have a garage?")
        self.taxes = input("What are your taxes on the house?")
        self.floors = input("How many floors in your house?")
class Coop(Habitat):
    def __init__(self):
        Habitat.__init__(self)
        self.parkingSpot = None
        self.carryingCharges = None
        self.cost = None
    def setCoop(self):
        self.parkingSpot = input("Does your Coop have a parking spot?")
        self.carryingCharges = input("What is your Coops monthly carrying charge?")
        self.cost = input("What did you pay for your Coop?")
class Apartment(Habitat):
    def __init__(self):
        Habitat.__init__(self)
        self.floor = None
        self.parkingSpot = None
        self.rent = None
    def setApartment(self):
        self.floor = input("How many floors are in your apartment?")
        self.parkingSpot = input("Does your apartment include a parking spot?")
        self.rent = input("What is your apartments monthly rent?")
house = House()
house.setHabitat()
house.setHouse()
coop = Coop()
coop.setHabitat()
coop.setCoop()
apartment=Apartment()
apartment.setHabitat()
apartment.setApartment()

