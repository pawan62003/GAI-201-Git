import json


class Snacks:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

# defined the json file name
inventory_file = "snacks_data.json"

## read the snacks data file;
try:
    with open(inventory_file, "r") as file:
        inventory_data = json.load(file)
except Exception as e:
    inventory_data = []
    print("Error occurred while reading the inventory file:", str(e))

# save inventory


def save_inventory():
    with open(inventory_file, "w") as file:
        data_to_save = [
            {"snack_id": snack["snack_id"], "name": snack["name"], "price": snack["price"], "availability": snack["availability"]}
            for snack in inventory_data
        ]
        json.dump(data_to_save, file, default=lambda obj: obj.__dict__)


# add a new snack

def add_snacks():
    snack_id = input("enter the snack id: ")
    name = input("enter the snack name: ")
    price = input("enter the snack price: ")
    availability = input("enter the snack availability: ").lower() == "yes"

    new_snack = Snacks(snack_id, name, price, availability)
    inventory_data.append(new_snack)
    save_inventory()
    print("snack added in inventory")


# remove a snack

def remove_snack():
    snack_id = input("enter the snack id: ")
    found = False
    for snack in inventory_data:
        if snack.snack_id == snack_id:
            inventory_data.remove(snack)
            found = True
            break

    if found:
        save_inventory()
        print("snack is removed")
    else:
        print("snack is not found")


# update inventory

def update_inventory():
    snack_id = input("enter the snack id: ")
    new_status = input("enter the new availability (yes/no): ")
    found = False

    for snack in inventory_data:
        if snack.snack_id == snack_id:
            snack.availability = new_status
            found = True
            break

    if found:
        save_inventory()
        print("snack updated successfully")
    else:
        print("snack is not found")


# sale record

def sale_record():
    snack_id = input("enter snack id for sale: ")
    found = False

    for snack in inventory_data:
        if snack.snack_id == snack_id:
            if snack.availability == "yes":
                snack.availability = "no"
                found = True
                break
            else:
                print("snack is not available")

    if found:
        save_inventory()
        print("snack is sold and availability is updated")
    else:
        print("snack is currently not available")


def welcome():
    print("Welcome to the Canteen Snack Inventory Management System!")
    print("1 Add snacks to the inventory")
    print("2 Remove snacks from the inventory.")
    print("3 Update the availability of snacks.")
    print("4 Record sales and update the inventory accordingly.")
    print("5 Exit")


loop = True

while True:
    print("\nCanteen Snack Inventory Management")
    print("===========================")
    for data in inventory_data:
        id_ = data["snack_id"]
        name = data["name"]
        price = data["price"]
        print(f"id: {id_} name: {name} , price: {price}")
        # print(data)
    print("===========================")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Snack Availability")
    print("4. Record Sale")
    print("5. Exit")
    print("===========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_snacks()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_inventory()
    elif choice == "4":
        sale_record()
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")