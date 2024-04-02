"""
This is Item module
"""

from dataclasses import dataclass, field


def increment() -> int:
    id_ = 0

    def inner():
        nonlocal id_
        id_ += 1
        return id_

    return inner


id_generator = increment()


@dataclass
class Item:
    """Example:
    >>> item = Item("The Godfather", "book", "living_room", 1)
    >>> item
    Item(name='The Godfather', category='book', place='living_room', quantity=1, id_=1)
    """

    name: str
    category: str
    place: str
    quantity: int = 1
    id_: int = field(init=False, default_factory=id_generator)

    def __contains__(self, text: str):
        """Example:
        >>> "the" in Item("The Godfather", "book", "living_room", 1)
        True
        """
        scope = self.name.split() + self.category.split() + self.place.split()
        scope = [t.lower() for t in scope]
        return True if text.lower() in scope else False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
