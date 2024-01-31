from employee import Employee
import pytest

@pytest.fixture
def employee():
    return Employee('John', 'Doe', 'Software Engineer', 140000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 145000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 150000

def test_give_custom_raise_negative(employee):
    employee.give_raise(-10000)
    assert employee.salary == 130000