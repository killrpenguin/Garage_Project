from objects import garage, car, truck


def title_info(auto_info=None) -> dict:
    if auto_info is None:
        fname = str(input("Enter Title Owners First Name: "))
        lname = str(input("Enter Title Owners Last Name: "))
        vname = str(input("What is the Vehicles Name?: "))
        seats = int(input("How many seats will it have?: "))
        capacity = str(input("Storage capacity in square feet?: "))
        auto_info = dict(fname=fname, lname=lname,
                         vname=vname, seats=seats, capacity=capacity)
    else:
        for i in auto_info:
            question = input("Current value: " + str(auto_info[i]) + " Change Value? (Y/N): ").upper()
            if question == "Y":
                new_value = input("New Value: ")
                auto_info.update({i: new_value})
    return auto_info


def create_garage(title_stuff=None) -> object:
    if title_stuff is None:
        title = title_info()
        obj = garage(title['fname'], title['lname'])
    else:
        obj = garage(title_stuff['fname'], title_stuff['lname'])
    return obj



def garage_project():
    title = title_info()
    garage_obj = create_garage(title)
    print(garage_obj.owner)

