from hypothesis import given
from hypothesis import strategies as st

from order import LineItem
from order import Order

@given(st.integers(), st.integers())
def test_line_item(price: int, quantity: int) -> None:
    line_item = LineItem("Apple", price, quantity)
    assert line_item.total == price * quantity

@given(st.text(), st.integers(), st.integers())
def test_order_line_item_idempotency(name: str, price: int, quantity: int) -> None:
    order = Order("John Doe", [])
    order.add_line_item(LineItem(name, price, quantity))
    order.add_line_item(LineItem(name, price, quantity))
    assert order.total == price * quantity
