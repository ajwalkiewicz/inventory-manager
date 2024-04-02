class ItemError(Exception):
    pass


class NameError(ItemError):
    pass


class CategoryError(ItemError):
    pass


class LocalizationError(ItemError):
    pass


class QuantityError(ItemError):
    pass
