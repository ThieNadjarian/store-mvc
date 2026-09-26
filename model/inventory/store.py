from model.inventory.stock import StockItem

class Shelf:
    def __init__(self, code: str):
        self._code = code
        self._items: list[StockItem] = []

    @property
    def code(self):
        return self._code
    
    @property
    def items(self):
        return list(self._items)

    #Adiciona o Item que eu quero ao Estoque
    def add_item(self, item: StockItem) -> None:
        self._items.append(item)

    #Dado um codigo eu procuro item no Estoque
    def find(self, sku: str) -> StockItem | None:
        for item in self._items:
            if str(item.product.sku) == sku:
                return item
        return None

    #Sting Legivel
    def __str__(self):
        return f"Shelf({self._code})"

    #Retorna Um objeto em formato de String
    def __repr__(self):
        return f"Shelf(code={self._code!r}, items={len(self._items)})"


class Aisle:
    def __init__(self, number: int):
        self._number  = number
        self._shelves: list[Shelf] = []

    @property
    def number(self):
        return self._number
    
    @property
    def shelves(self):
        return list(self._shelves)

    #Adiciona um Item a Pratileira
    def add_shelf(self, shelf: Shelf) -> None:
        self._shelves.append(shelf)

    #Procura um item no Estoque a partir da Pratileira
    def find(self, sku: str) -> StockItem | None:
        for shelf in self._shelves:
            item = shelf.find(sku)
            if item:
                return item
        return None

    def __str__(self):
        return f"Aisle {self._number}"
    
    def __repr__(self):
        return f"Aisle(number={self._number}, shelves={len(self._shelves)})"