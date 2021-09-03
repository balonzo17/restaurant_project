# Create resturant class

class restaurant:


    def __init__(self, menu = {}, customer = {}, order = {}):
        self.menu = menu 
        self.customer = customer
        self.order = order 


#  INTERACTIVE METHODS
    def open(self):
        new_customer={}
        new_customer["Lucas"] = input("Welcome to my grub spot! What's your name?")
        new_customer["email"] = input("May i have your email address, please")
        self.add_customer(new_customer["Lucas"], new_customer["lucas_zapboy@dc.com"])

# MENU METHODS 
def add_menu(self, menu_name, menu):
    self.menus[menu_name] = menu

def add_menu_item(self, menu_name, item_name, item):
    self.menus[menu_name][item_name] = item

def remove_menu_items(self, menu_name, item_name):
    del self.menus[menu_name]["items"][item_name]

def change_item_price(self, menu_name, item_name, new_price):
    self.menus[menu_name]["items"][item_name]["price"] = new_price


# CUSTOMER METHODS
def add_customer(self, name, email, available_funds = 100):
    customer = {
        "name": name,
        "email": email, 
        "available_funds": available_funds
    }

    self.customer [name] = customer 
new_restaurant = restaurant()   
new_restaurant.open()
print("CUSTOMER")
print(new_restaurant.customer)

print(new_restaurant.menus)
#Shoud be empty at this point

new_restaurant.add_menus("breakfast", {
        "items": {
            "Frech_toast": {
            
                "price": 12
            }, 
        "Omellette": {
            "price": 18
        },
        "pancakes": {
            "price": 15
        }
 }
 })

new_restaurant.add_menus("lunch", {
    "items": {
        "sandwich": {
            "price": 20
        },
        "curly_fries": {
            "price": 25
        },
        "salmon": {
            "price": 35
        }
    }
    
})

new_order = order(True)

new_order.add_customer_name("Lucas")

new_order.add_item({
    "name": "French_toast",
    "price": 12
})

new_order.add_item({
    "name": "curly_fries", 
    "price": 25
 })

new_order.get_total_price()
new_order.get_total_price()








