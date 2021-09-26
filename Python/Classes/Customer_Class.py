class Customer: # create customer class
  def __init__(self,CustomerName,CustomerAddress1,City,State,ZipCode): # Add customer attributes
    self.CustomerName = CustomerName 
    self.CustomerAddress1 = CustomerAddress1
    self.City = City
    self.State = State
    self.ZipCode = ZipCode
# Define Customer attribute information
p1 = Customer("Steve Sanders", "1122 Arlington Way","Memphis","TN","37501")
p2 = Customer("Alex Smith", "123 Webster St","Kansas City","MO","64119")
p3 = Customer("Charlie Rhoades", "789 Agave Pl","Denver","CO","80014")
p4 = Customer("Gilbert Song", "5566 Eggshell Rd","Seattle","WA","98101")
p5 = Customer("Billy Granger", "8877 Nemo Blv","Houston","TX","77001")
p6 = Customer("Bob Baker", "963 Yellowstone Dr","Topeka","KS","66546")
p7 = Customer("Ashley Ellis", "258 Buford Way","Tampa","FL","33601")
p8 = Customer("Brittney Biggs", "7859 Wilson St","Santa Cruz","CA","95060")
p9 = Customer("Jillian Spears", "7141 Jetty Dr","Portland","OR","97035")
p10 = Customer("Heather Blair", "3256 Keller Pl","Boston","MA","02101")
p11 = Customer("Jenny Stitch", "2563 Evergreen St","Santa Fe","NM","87501")
p12 = Customer("Joseph Flanders", "8956 Smokehouse Rd","Wrens","GA","30833")
p13 = Customer("Jason Starling", "492 Dusty Bluff Way","Park City","UT","84098")
p14 = Customer("Taylor Sprig", "4422 Sunset St","Charlotte","NC","28126")
p15 = Customer("Allison Spaulding", "8956 Palm Rd","Tombstone","AZ","85638")

# Assign customer zip code attribute to an array.
zips = [p1.ZipCode,p2.ZipCode,p3.ZipCode,p4.ZipCode,p5.ZipCode,p6.ZipCode,p7.ZipCode,p8.ZipCode,p9.ZipCode,p10.ZipCode,p11.ZipCode,p12.ZipCode,p13.ZipCode,p14.ZipCode,p15.ZipCode]
# Print array
print("The zip codes for these customers are, ", zips)