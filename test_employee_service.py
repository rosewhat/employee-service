import pytest
from app.api.models import EmployeeIn, EmployeeOut

employee = EmployeeIn(
    name='Anton',
    surname='Russian',
    age='21',
    phone='+7123456789'
)


def test_create_employee(employee: EmployeeIn = employee):
    assert dict(employee) == {'name': employee.name,
                              'surname': employee.surname,
                              'age': employee.age,
                              'phone': employee.phone
                              }

'''
def test_update_employee_age(employee: EmployeeIn = employee):
    employee_upd = EmployeeOut(
        name='Anton',
        surname='Russian',
        age='22',
        phone='+7123456789',
        id=1
    )
    assert dict(employee_upd) == {'name': cast.name,
                              'nationality': cast.nationality,
                              'id': cast_upd.id
                              }


def test_update_cast_genre(employee: EmployeeIn = employee):
    cast_upd = EmployeeOut(
        name=cast.name,
        nationality=cast.nationality,
        id=1
    )
    assert dict(cast_upd) == {'name': cast.name,
                              'nationality': cast.nationality,
                              'id': cast_upd.id}
'''