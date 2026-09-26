from model.product import Product
from model.identity import Customer

class LineItem:
    def __init__(self, product: Product, quantity: int):
        self._product = product
        self._quantity = quantity

    @property
    def product(self):
        return self._product
    
    @property
    def quantity(self):
        return self._quantity

    def subtotal(self) -> float:
        return self._product.price * self._quantity

    def __str__(self):
        return f"{self._product.name} x {self._quantity} = R$ {self._product.final_price():.2f}"

    def __repr__(self):
        return f"LineItem(sku={self._product.sku!r}, qty={self._quantity})"

class Cart:
    def __init__(self, customer: Customer):
        self._customer = customer
        self._items: list[LineItem] = []

    @property
    def customer(self):
        return self._customer
    
    @property
    def items(self):
        return list(self._items)

    def add(self, product: Product, qty: int) -> None:
        achou = False
        posicao = 0

        #for item in self._items:
        while posicao < len(self._items) and not achou:
            #Item esta pegando o item dql posicao da lista
            item = self._items[posicao]

            if item.product.sku == product.sku:
                achou = True
                qty += item.quantity
                item_substituido = LineItem(product, qty)
                #Caso ache o item que esta no carrino faz a substituicao dele na mesma posição
                self._items[posicao] = item_substituido

            posicao += 1

        if not achou:
            self._items.append(LineItem(product, qty))

    def remove(self, sku: str) -> None:
        self._items = [i for i in self._items if str(i.product.sku) != sku]

    def total(self) -> float:
        return sum(i.subtotal() for i in self._items)

    def __str__(self):
        lines = "\n".join(f"  {i}" for i in self._items)
        return f"Cart [{self._customer.name}]\n{lines}\n  Total: R$ {self.total():.2f}"

