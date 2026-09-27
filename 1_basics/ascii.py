from functools import reduce
from hypothesis import given
from hypothesis import strategies as st
from hypothesis import example
from hypothesis import settings


def to_ascii_codes(input: str) -> list[int]:
    return [ord(c) for c in input]

def from_ascii_codes(input: list[int]) -> str:
    return reduce(lambda x, y: x + chr(y), input, "")


@given(st.text())
@example("")
@settings(max_examples=100)
def test_reversibility_of_ascii_codes(input: str) -> None:
    assert from_ascii_codes(to_ascii_codes(input)) == input

@given(st.text())
@example("")
@settings(max_examples=100)
def test_input_length_is_same_as_encoded_length(input: str) -> None:
    assert len(to_ascii_codes(input)) == len(input)
