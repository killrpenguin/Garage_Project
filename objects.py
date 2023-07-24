"""This week we will work with classes by creating virutal garage.
Your program will use the inheritance diagram below in order to
 create a parent class and two child classes.

 Your program will prompt the user to create at least one object of each type (Car and Pickup).
 Using a menu system and capturing user input. Your program will allow the user the choice of
 adding a car or picking up track and define the vehicles attributes.
 The program will use user input to define the vehicles attributes.
 """
class garage:
    def __init__(self, owner_fname, owner_lname, address, phone_num):
        self.owner_fname = owner_fname
        self.owner_lname = owner_lname
        self.address = address
        self.phone_num = phone_num
        self.owner = str(owner_fname) + " " + str(owner_lname)
        self.storage = []

    def park_vehicle(self, vehicle):
        self.storage.append(vehicle)

    def sell_vehicle(self, vehicle):
        self.storage.remove(vehicle)

    def check_garage(self):
        for i in self.storage:
            print(i.owner + " " + i.v_name)


class car(garage):
    def __init__(self, owner_fname, owner_lname, make, model, seats, milage, vin):
        super().__init__(owner_fname, owner_lname, address, phone_num)
        self.make = make
        self.model = model
        self.seats = seats
        self.milage = milage
        self.vin = vin


class truck(garage):
    def __init__(self, owner_fname, owner_lname, make, model, seats, milage, vin):
        super().__init__(owner_fname, owner_lname, address, phone_num)
        self.make = make
        self.model = model
        self.seats = seats
        self.milage = milage
        self.vin = vin
