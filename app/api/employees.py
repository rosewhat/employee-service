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


@employees.get('/{id}/', response_model=EmployeeOut)
async def get_employee(id: int):
    company = await db_manager.get_employee(id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@employees.delete('/{id}/', response_model=None)
async def delete_employee(id: int):
    company = await db_manager.get_employee(id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return await db_manager.delete_employee(id)