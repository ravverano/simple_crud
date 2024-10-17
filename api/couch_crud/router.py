from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db_session import get_cdb
from .controller import crud as controller
from .schema import (
    GetData,
    CreateData,
    UpdateData

)
router = APIRouter()

@router.get("/crud")
def get_data(
    *,
    cdb: Session = Depends(get_cdb),
    query_params: GetData = Depends()
):
    return controller.get_data(cdb, query_params)

@router.post("/crud")
def create_data(
    *,
    cdb: Session = Depends(get_cdb),
    query_params: CreateData,
):
    return controller.create_data(cdb, query_params)

@router.put("/crud")
def update_data(
    *,
    cdb: Session = Depends(get_cdb),
    query_params: UpdateData,
):
    return controller.update_data(cdb, query_params)

@router.delete("/crud")
def delete_data(
    *,
    cdb: Session = Depends(get_cdb),
    data_id: str
):
    return controller.delete_data(cdb, data_id)

