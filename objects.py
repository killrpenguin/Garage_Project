class garage(object):
    def __init__(self, owner_fname, owner_lname, address, phone_num):
        self.owner_fname = owner_fname
        self.owner_lname = owner_lname
        self.address = address
        self.phone_num = phone_num
        self.owner = str(owner_fname) + " " + str(owner_lname)
        self.storage = []

    def add_vehicle(self, vehicle):
        self.storage.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.storage.remove(vehicle)

    def disp_inventory(self):
        for i in self.storage:
            print(i.owner + " " + i.make)


class car(garage):
    def __init__(self, owner_fname, owner_lname, address, phone_num, make, model, seats, milage, vin):
        super().__init__(owner_fname, owner_lname, address, phone_num)
        self.make = make
        self.model = model
        self.seats = seats
        self.milage = milage
        self.vin = vin


class truck(garage):
    def __init__(self, owner_fname, owner_lname, address, phone_num, make, model, seats, milage, vin):
        super().__init__(owner_fname, owner_lname, address, phone_num)
        self.make = make
        self.model = model
        self.seats = seats
        self.milage = milage
        self.vin = vin