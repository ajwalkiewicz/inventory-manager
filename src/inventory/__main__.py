import pickle
import sys
import threading

from inventory.controler.controler import InventoryControler
from inventory.inventory.inventory import Inventory
from inventory.server.server import Server


class Editor:
    def __init__(self, inventory: Inventory):
        self.menu_options = {
            "1": self.add_item,
            "2": self.remove,
            "3": self.show_items,
            "4": self.search_item,
            "5": self.save_work,
            "6": self.exit,
        }
        self.inventory = inventory

    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
1. add item
2. remove item
3. show items
4. search item
5. save work
6. exit
"""
                )
                answer = input("enter a command: ")
                try:
                    func = self.menu_options[answer]
                except KeyError:
                    print(f"'{answer}'' is not a valid option")
                else:
                    func()
        finally:
            print("Thank you for using Inventory Manager")

    def add_item(self):
        print("Enter item: (name category localization quantity")
        name, category, place, quantity = input().split()
        quantity = int(quantity)
        new_item = self.inventory.create_item(name, category, place, quantity)
        self.inventory.add(new_item)
        print("Added new Item:")
        print(self._print_item(new_item))

    def remove(self):
        index = input("Enter item id: ")
        for item in self.inventory.inventory:
            if item.id_ == int(index):
                self.inventory.remove(item)
                print("Item removed")
                break
        else:
            print("Item not found")

    def save_work(self):
        with open("database", "wb") as database:
            pickle.dump(self.inventory, database)
        print("Work saved")

    def show_items(self):
        for nr, item in enumerate(self.inventory.inventory):
            print(self._print_item(item, nr))

    def search_item(self):
        text = input("Search: ")
        for nr, item in enumerate(self.inventory.search(text)):
            print(self._print_item(item, nr))
        print("Found Items")

    def _print_item(self, item, nr: int = 0):
        return f"""
--------------------------------
nr {nr+1}
name: {item.name}
category: {item.category}
place: {item.place}
quantity: {item.quantity}
id: {item.id_}
--------------------------------
"""

    def exit(self):
        sys.exit("Exiting...")


if __name__ == "__main__":
    print("Welcome in Inventory Menager")
    try:
        print("Loading database")
        with open("database", "rb") as database:
            inventory = pickle.load(database)
    except FileNotFoundError:
        print("Database not found, creating a new one")
        inventory = Inventory()
        with open("database", "wb") as database:
            pickle.dump(inventory, database)

    editor = Editor(inventory=inventory)
    inventory_controler = InventoryControler(inventory=inventory)
    server = Server(inventory_controler=inventory_controler)

    threading.Thread(target=server.start).start()
    threading.Thread(target=editor.menu).start()
