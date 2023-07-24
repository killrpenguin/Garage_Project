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


def garage_project():
    garage_details = get_garage_info()
    garage_obj = create_garage(garage_details)
    print(garage_obj.owner)
    print(garage_obj.address)
    print(garage_obj.phone_num)


garage_project()