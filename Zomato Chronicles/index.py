import json

# read the file
def read_menu_from_file(filename):
    with open(filename,"r") as file:
        return json.load(file)
    
menu = read_menu_from_file("data.json")

# write the file
def write_menu_to_file(menu,filename):
    with open(filename,"w") as file:
        json.dump(menu, file, indent=4)

class Order:
    def __init__(self,order_id,customer_name,dishes):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = 'received'

# class zomato:
#       def __init__(self,_id,name,price,availability):
#             self._id = _id
#             self.name = name
#             self.price = price
#             self.availability = availability

def display_menu():
      for menu_item in menu:
            id_ = menu_item["_id"]
            name = menu_item["name"]
            price = menu_item["price"]
            print(f"id: {id_} name:{name} price:{price}")
      print("===================================")

# add a new dish in menu
def add_dish():
      _id = input("enter the new dish id : ")
      name = input("enter the new dish name : ")
      price = input("enter the dish price : ")
      availability = input("enter the availability : ")

      new_dish = {
            "_id":_id,
            "name":name,
            "price":price,
            "availability":availability
      }

      menu.append(new_dish)
      write_menu_to_file(menu,"data.json")
      print("===============================")
      print("new dish added in database")
      print("===============================")

def remove_dish():
    dish_id = input("Which dish you want to remove: ")
    found = False
    to_remove = []

    for item in menu:
        if item["_id"] == dish_id:
            to_remove.append(item)
            found = True

    for item in to_remove:
        menu.remove(item)

    if found:
        write_menu_to_file(menu,"data.json")
        print("Dish is removed")
    else:
        print("Dish is not found")
    print("===============================")


orders = {}
# update availability
def update_availability():
     item_id = input("please enter the id : ")
     new_status = input("enter the new availability (yes/no): ")

     found = False

     for item in menu:
          if item["_id"] == item_id:
               item["availability"] = new_status
               found = True
               
     if found:
          write_menu_to_file(menu,"data.json")
          print("item is updated")
     else:
          print("please enter a valid id")
     print("=============================")

def take_order_from_user(menu):
    customer_name = input("Enter customer name: ")
    dish_ids = [input(f"Enter dish ID for dish {i+1}: ") for i in range(len(menu))]
    
    dishes = []
    for dish_id in dish_ids:
        dish = next((item for item in menu if item["_id"] == dish_id and item["availability"] == "yes"), None)
        if dish:
            dishes.append(dish)
        else:
            print(f"Dish with ID {dish_id} is not available.")
            return
    
    order_id = len(orders) + 1
    order = Order(order_id, customer_name, dishes)
    orders[order_id] = order
    print(f"Order received! Order ID: {order_id}")
    print("===============================")


while True:
    print("\nZesty Zomato Operations:")
    print("================================")
    print("1. Display Menu")
    print("2. Add Dish to Menu")
    print("3. Remove Dish from Menu")
    print("4. Update Dish Availability")
    print("5. Take Order")
    print("6. Exit")
    print("==================================")

    choice = input("Select an option: ")
    print("===================================")
    # Handle user's choice
    if choice == "1":
        display_menu()
    elif choice == "2":
        add_dish()
    elif choice == "3":
          remove_dish()
    elif choice == "4":
         update_availability()
    elif choice == "5":
        take_order_from_user(menu)
    elif choice == "6":
        print("Exiting Zesty Zomato. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
