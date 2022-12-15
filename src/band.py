class Band:
    def __init__(self, name : str, width : int, price : int):
        self.name = name
        self.width = width
        self.price = price

    def __str__(self) -> str:
        return self.name