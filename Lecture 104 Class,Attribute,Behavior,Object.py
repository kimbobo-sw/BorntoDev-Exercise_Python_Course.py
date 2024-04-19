class Customer:
    name =""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,self.age,"'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 23
customer1.addCart()

customer2 = Customer()
customer2.name = "kim"
customer2.lastName = "Baby"
customer2.age = 22
customer2.addCart()

customer3 = Customer()
customer3.name = "sawlaw"
customer3.lastName = "Nilan"
customer3.age = 21
customer3.addCart()

customer4 = Customer()
customer4.name = "Aummilo"
customer4.lastName = "swowat"
customer4.age = 20
customer4.addCart()