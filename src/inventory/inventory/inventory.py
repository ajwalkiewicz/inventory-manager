"""
This is inventory module

Example:
>>> inv = Inventory()
>>> item = Item("The Godfather", "book", "living_room", 1)
>>> type(item)
<class 'item.Item'>
>>> isinstance(item, Item)
True
"""

import inventory.errors.errors as errors
from inventory.inventory.item import Item


class Inventory:
    def __init__(self):
        self.inventory = []
        self.created_items = []
        self.ammount = 0

    def create_item(self, name: str, category: str, place: str, quantity: int):
        """Examples:
        >>> inv.create_item("Arduino", "electronics", "Kid's room", 0)
        Item(name='Arduino', category='electronics', place="Kid's room", quantity=0)
        >>> inv.create_item("Arduino", "electronics", "Kid's room", "0")
        QuantityError: '0' is not a Int
        False
        >>> inv.create_item("Arduino", "electronics", "Kid's room", -1)
        QuantityError: Quantity cannot be less then 0
        False
        >>> inv.create_item("", "electronics", "Kid's room", 1)
        NameError: cannot be empty
        False
        >>> inv.create_item("Arduino", 123, "Kid's room", 1)
        CategoryError: '123' is not a Str
        False
        """
        try:
            if not isinstance(quantity, int):
                raise errors.QuantityError(f"'{quantity}' is not a Int")
            if quantity < 0:
                raise errors.QuantityError(f"Quantity cannot be less then 0")

            for index, attribute in enumerate([name, category, place]):
                error = [
                    errors.NameError,
                    errors.CategoryError,
                    errors.LocalizationError,
                ][index]
                if not isinstance(attribute, str):
                    raise error(f"'{attribute}' is not a Str")
                if not attribute:
                    raise error("cannot be empty")

        except errors.QuantityError as e:
            print(f"{e.__class__.__name__}: {e.args[0]}")
            return False
        except errors.NameError as e:
            print(f"{e.__class__.__name__}: {e.args[0]}")
            return False
        except errors.CategoryError as e:
            print(f"{e.__class__.__name__}: {e.args[0]}")
            return False
        except errors.LocalizationError as e:
            print(f"{e.__class__.__name__}: {e.args[0]}")
            return False
        else:
            item = Item(name, category, place, quantity)
            self.created_items.append(item)
            return item

    def add(self, item: Item) -> bool:
        """Add item to the inventory. Examples:
        >>> item = Item("The Godfather", "book", "living_room", 1)
        >>> Inventory().add(item)
        True
        >>> Inventory().add("Item")
        ValueError: Item ('Item',) is not an Item
        False
        """
        try:
            if not isinstance(item, Item):
                raise ValueError(item)
            self.inventory.append(item)
        except ValueError as e:
            print(f"{e.__class__.__name__}: Item {e.args} is not an Item")
            return False
        else:
            self.ammount += item.quantity
            return True

    def remove(self, item: Item) -> bool:
        """Examples:
        >>> inv.inventory = []
        >>> item = Item("The Godfather", "book", "living_room", 1)
        >>> inv.add(item)
        True
        >>> inv.remove(item)
        True
        >>> inv.remove(item)
        ValueError: Item The Godfather is not in Inventory
        False
        """
        try:
            self.inventory.remove(item)
        except ValueError as e:
            print(f"{e.__class__.__name__}: Item {item.name} is not in Inventory")
            return False
        else:
            self.ammount -= item.quantity
            return True

    def get_ammount(self) -> int:
        """Examples:
        >>> item = Item("The Godfather", "book", "living_room", 1)
        >>> inv.add(item)
        True
        >>> inv.get_ammount()
        1
        """
        return self.ammount

    def search(self, text: str) -> list[Item]:
        """Examples:
        >>> inv.add(Item("The Godfather", "book", "living_room", 1))
        True
        >>> inv.add(Item("Poor dad Rich dad", "book", "living_room", 2))
        True
        >>> inv.add(Item("Yo Dad", "CD", "living_room", 4))
        True
        >>> inv.search("dad")
        [Item(name='Poor dad Rich dad', category='book', place='living_room', quantity=2), Item(name='Yo Dad', category='CD', place='living_room', quantity=4)]
        """
        result = []

        for item in self.inventory:
            if text in item:
                result.append(item)

        return result

    def modify(self, item):
        pass


if __name__ == "__main__":
    import doctest

    inv = Inventory()
    doctest.testmod()
