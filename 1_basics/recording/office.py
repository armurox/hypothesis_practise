import random
from enum import Enum, auto
from hypothesis import strategies as st

class Employee(Enum):
    """Employee type"""
    
    CEO = auto()
    MANAGER = auto()
    SALES = auto()
    ENGINEER = auto()
    MARKETING = auto()
    ACCOUNTING = auto()
    IT = auto()
    HR = auto()
    OTHER = auto()
    

def generate_random_team(size: int) -> list[Employee]:
    """Generate a random team with exactly one CEO"""
    if size <= 0:
        raise ValueError("Team size should be larger than 0")
    employees_no_ceo = list(Employee)
    employees_no_ceo.remove(Employee.CEO)
    team = []
    for _ in range(size - 1):
        team.append(random.choices(employees_no_ceo))
    team.append(Employee.CEO)
    return team

def fire_random_employee(team: list[Employee]) -> None:
    team_no_ceo = team.copy()
    team_no_ceo.remove(Employee.CEO)
    if len(team_no_ceo) > 0:
        team.remove(random.choice(team_no_ceo))
    else:
        team.remove(Employee.CEO)
    

# SIZE = 4
# team = generate_random_team(SIZE) 
# print(team)
# for i in range(SIZE):
#     print('Firing random employee', i + 1)
#     fire_random_employee(team)
#     print('Team after firing is', team)
