from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import EmployeeOut, EmployeeIn
from app.api import db_manager

employees = APIRouter()

@employees.post('/', response_model=EmployeeOut, status_code=201)
async def create_employee(payload: EmployeeIn):
    employee_id = await db_manager.add_employee(payload)

    response = {
        'id': employee_id,
        **payload.dict()
    }

    return response


@employees.get('/', response_model=List[EmployeeOut])
async def get_employees():
    return await db_manager.get_all_employee()

'''
@employees.put('/{id}/', response_model=EmployeeOut)
async def update_employee(id: int, payload: CompanyUpdate):
    employee = await db_manager.get_company(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Company not found")

    update_data = payload.dict(exclude_unset=True)

    employee_in_db = EmployeeIn(**employee)

    updated_employee = employee_in_db.copy(update=update_data)

    return await db_manager.update_employee(id, updated_employee)
'''
@employees.delete('/{id}/', response_model=None)
async def delete_employee(id: int):
    company = await db_manager.get_company(id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return await db_manager.delete_company(id)