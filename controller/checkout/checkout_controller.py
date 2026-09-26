from checkout import Order
from model.checkout import Order, Cart
from model.identity import Customer
from model.product import Product
from view.checkout.checkout_view import CheckoutView

class CheckoutController:
    def __init__(self, view: CheckoutView):
        self._cart: Cart | None = None
        self._orders: list[Order] = []
        self._view = view

    def open_cart(self, customer: Customer) -> None:
        self._cart = Cart(customer)

    def add_item(self, product: Product, qty: int) -> None:
        if not self._cart:
            raise ValueError("No open cart")
        self._cart.add(product, qty)
        self._view.show_cart(self._cart)

    def confirm(self) -> Order | None:
        #self._view.show_cart(self._cart)
        if not self._cart:
            raise ValueError("No open cart")

        else :self._view.show_cart(self._cart)
        if self._view.confirm_prompt():
            self._view.thanks()
            order = Order(self._cart)
            self._orders.append(order)
            self._view.show_order(order)
            return order
        return None

    def advance(self) -> None:
        if not self._orders:
            raise ValueError("No orders")

        else:
            for order in self._orders:
                order.advance_status()
                self._view.show_status(order)