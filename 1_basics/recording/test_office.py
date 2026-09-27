from typing import Callable
from hypothesis import given
from hypothesis import strategies as st
from hypothesis import settings
import pytest
from office import generate_random_team
from office import fire_random_employee
from office import Employee

@st.composite
def teams(draw: Callable[[st.SearchStrategy[int]], int], min_value: int = 1, max_value: int = 20) -> list[Employee]:
    rand_value = draw(st.integers(min_value, max_value))
    return generate_random_team(rand_value)

@given(st.integers(min_value=-20, max_value=0))
def test_negative_team_size(team_size: int):
    with pytest.raises(ValueError):
        generate_random_team(team_size)


@given(st.integers(min_value=1, max_value=20))
def test_team_size(team_size: int) -> None:
    assert len(generate_random_team(team_size)) == team_size

@given(teams())
def test_team_has_ceo(teams: list[Employee]) -> None:
    assert Employee.CEO in teams

@given(teams())
def test_team_size_reduce_by_one_when_firing(team: list[Employee]) -> None:
    original_team_size = len(team)
    fire_random_employee(team)
    assert original_team_size - len(team) == 1