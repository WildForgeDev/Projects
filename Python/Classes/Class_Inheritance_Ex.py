class Vehical: #Create base class vehical
    def __init__(self): #Create self object
        self.doors = None # Define door attribute
        self.enginetype = None # Define enginetype attribute
        self.color  = None # Define color attribute
        self.price = None # Define price attribute
    def setVehical(self): #Create function for base class Vehical self object
        self.doors = input("How many doors on vehical?: ") # Get User input for doors attribute.
        self.enginetype = input("what type of engine does this vehical have?: ") # Get User input for engine attribute.
        self.color = input("What color is this vehical?: ") # Get User input for color attribute.
        self.price = input("What is the price of this vehical?: ") # Get User input for price attribute.
class Car(Vehical): #Create subclass of Vehical as Car
    def __init__(self): #Create self object
        Vehical.__init__(self) #Create self object of Car subclass
        self.cartype = None # Create cartype attribute of Car subclass
        self.warranty = None # Create warranty attribute of Car subclass
        self.drivetrain = None # Create drivetrain attribute of Car subclass
    def setCar(self): #Create setCar function of Car subclass
        self.cartype = input("What type of car is this?: ") # Get User input for cartype attribute for car subclass.
        self.warranty = input("How long does the included warranty cover this car?: ") # Get User input for warranty attribute for car subclass.
        self.drivetrain = input("what kind of drivetrain does this car have?: ") # Get User input for drivetrain attribute for car subclass.
        self.color = input("What color is this car?: ") # Get User input for inherited color attribute for car subclass.
class Truck(Vehical): #Create subclass of Vehical as Truck
    def __init__(self): #Create self object
        Vehical.__init__(self) #Create self object of Truck subclass
        self.fourwheeldrive = None # Create fourwheeldrive attribute of Truck subclass
        self.fueltype = None # Create fueltype attribute of Truck subclass
        self.extendedbed = None # Create extendedbed attribute of Truck subclass
    def setTruck(self): #Create setTruck function of Truck subclass
        self.fourwheeldrive = input("Is this truck four wheel drive?: ") # Get User input for fourwheeldrive attribute for Truck subclass.
        self.fueltype = input("Does this truck use gas or diesel?: ") # Get User input for fueltype attribute for Truck subclass.
        self.extendedbed = input("Does this truck have an extended bed?: ") # Get User input for extended attribute for Truck subclass.
        self.doors = input("How many doors does this truck have?: ") #Get User input for inherited color attribute for Truck subclass.
class Boat(Vehical): # Create subclass of Vehical as Boat
    def __init__(self): # Create self object
        Vehical.__init__(self) # Create self object of Boat subclass
        self.length = None # Create length attribute of Boat subclass
        self.boattype = None # Create boattype attribute of Boat subclass
        self.enginetype = None # Create enginetype attribute of Boat subclass
    def setBoat(self): #Create setBoat function of Boat subclass
        self.length = input("How long is this boat?: ") # Get User input for length attribute for Boat subclass.
        self.boattype = input("What type of boat is this?: ") # Get User input for boattype attribute for Boat subclass.
        self.price = input("How much does this boat cost?: ") # Get User input for price attribute for Boat subclass.
        self.enginetype = input("What type of engine does this boat have?: ") #Get User input for inherited enginetype attribute for Truck subclass.
car = Car() #Create car variable and set it as created Car list
car.setVehical() #Invoke car variable with the setVehical function
car.setCar() #Invoke car variable with setCar function
truck = Truck() #Create truck variable and set it as created Truck list
truck.setVehical() #Invoke truck variable with setVehical function
truck.setTruck() #Invoke truck variable with setTruck function
boat=Boat() #Create boat variable and set it as created Boat list
boat.setVehical() #Invoke boat variable with setVehical function
boat.setBoat() #Invoke bruck variable with setTruck function