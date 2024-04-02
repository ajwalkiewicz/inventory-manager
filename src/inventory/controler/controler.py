from inventory.inventory.inventory import Inventory, Item


class InventoryControler:

    def __init__(self, inventory: Inventory | None = None) -> None:
        if inventory is None:
            self.inventory = Inventory()
        else:
            self.inventory = inventory

    def add_item(self, name: str, category: str, place: str, quantity: int):
        item = Item(name, category, place, quantity)
        return self.inventory.add(item)

    def remove_item(self, id_: int) -> Item:
        item = [item for item in self.inventory.inventory if item.id_ == id_][0]
        return self.inventory.remove(item)

    def get_items(self):
        return self.inventory.inventory

    def execute(self, command: dict):
        try:
            # method = getattr(self.inventory, command.get("method"))
            method = getattr(self, command.get("method"))
            args = command.get("args")
            if args is None:
                return method()
            return method(*args)
        except (AttributeError, TypeError) as e:
            return e
