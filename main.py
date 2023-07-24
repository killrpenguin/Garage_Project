from objects import garage, car, truck


def title_info(auto_info=None) -> dict:
    if auto_info is None:
        fname = str(input("Enter Title Owners First Name: "))
        lname = str(input("Enter Title Owners Last Name: "))
        vname = str(input("What is the Vehicles Name?: "))
        seats = int(input("How many seats will it have?: "))
        capacity = input("Storage capacity in square feet?: ")
        auto_info = dict(fname=fname, lname=lname,
                         vname=vname, seats=seats,
                         capacity=capacity)
    else:
        for i in auto_info:
            print(auto_info[i])
    return auto_info

def create_garage(list=None) -> object:
    if list is None:
        title_info()
    else:
        car_house = garage(["fname"], ["lname"])
    return car_house



def garage_project():
    # while loop will go here.
    pass


tmp = title_info()
title_info(tmp)
