from hypothesis import given
from hypothesis import strategies as st

from order import LineItem

@given(st.integers(), st.integers())
def test_line_item(price: int, quantity: int) -> None:
    line_item = LineItem("Apple", price, quantity)
    assert line_item.total == price * quantity
