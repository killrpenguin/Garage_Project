from objects import garage, car, truck


def get_garage_info(garage_owner=None) -> dict:
    if garage_owner is None:
        fname = str(input("Enter Garage Owners First Name: "))
        lname = str(input("Enter Garage Owners Last Name: "))
        address = str(input("Enter the address of the garage: "))
        phone_num = str(input("Enter the Phone number of the garage: "))
        garage_owner = dict(fname=fname, lname=lname,
                            address=address, phone_num=phone_num)
    else:
        for i in garage_owner:
            question = input("Current value: " + str(garage_owner[i]) + " Change Value? (Y/N): ").upper()
            if question == "Y":
                new_value = input("New Value: ")
                garage_owner.update({i: new_value})
    return garage_owner


def create_garage(garage_stuff=None) -> object:
    if garage_stuff is None:
        title_details = get_garage_info()
        obj = garage(title_details['fname'], title_details['lname'],
                     title_details['address'], title_details['phone_num'])
    else:
        obj = garage(garage_stuff['fname'], garage_stuff['lname'],
                     garage_stuff['address'], garage_stuff['phone_num'])
    return obj


def vehicle_info() -> dict:
    vehicle_type = str(input("Is this a Car or Truck?: ")).upper()
    make = str(input("Enter the make of the vehicle "))
    model = str(input("Enter the model of the vehicle: "))
    seats = int(input("How many seats in the vehicle: "))
    milage = float(input("How many miles does it have?: "))
    vin = str(input("What is the vin number of the vehicle?: "))
    vehicle = dict(vehicle_type=vehicle_type, make=make, model=model,
                   seats=seats, milage=milage, vin=vin)
    return vehicle


def get_vehicle_obj(vehicle_details, garage_details) -> object:
    if vehicle_details['vehicle_type'] == "CAR":
        obj = car(garage_details['fname'], garage_details['lname'], garage_details['address'],
                  garage_details['phone_num'], vehicle_details['make'], vehicle_details['model'],
                  vehicle_details['seats'], vehicle_details['milage'], vehicle_details['vin'])
    elif vehicle_details['vehicle_type'] == "TRUCK":
        obj = truck(garage_details['fname'], garage_details['lname'], garage_details['address'],
                  garage_details['phone_num'], vehicle_details['make'], vehicle_details['model'],
                  vehicle_details['seats'], vehicle_details['milage'], vehicle_details['vin'])
    return obj


def menu() -> str:
    user_input = str(input("""
    1. Add Vehicle
    2. Remove Vehicle
    3. List Owned Vehicles
    4. Edit Garage Information
    5. Save Garage Information
    6. Exit
    """))
    return user_input


def garage_project():
    garage_details = get_garage_info()
    garage_obj = create_garage(garage_details)
    start = str(input("Manage your Garage? (Y/N): ")).upper()
    while start == 'Y':
        user_action = menu()
        if user_action == "1":
            vehicle_info = vehicle_info()
            vehicle = get_vehicle_obj(vehicle_info, garage_details)
            garage_obj.add_vehicle(vehicle)
        elif user_action == "2":
            pass
        elif user_action == "3":
            garage_obj.disp_inventory()
        elif user_action == "4":
            # This currently clears inventory. Find a way to copy old object list to new object list.
            garage_details = get_garage_info(garage_details)
            garage_obj = create_garage(garage_details)
        elif user_action == "5":
            pass
        elif user_action == "6":
            break


garage_project()