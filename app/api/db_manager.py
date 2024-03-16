from app.api.models import EmployeeIn, EmployeeOut
from app.api.db import employees, database


async def add_employee(payload: EmployeeIn):
    query = employees.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_employee():
    query = employees.select()
    return await database.fetch_all(query=query)


async def delete_employee(id: int):
    query = employees.delete().where(employees.c.id == id)
    return await database.execute(query=query)


async def update_employee(id: int, payload: EmployeeIn):
    query = (
        employees
        .update()
        .where(employees.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)