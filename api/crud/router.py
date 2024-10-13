from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db_session import get_db
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
    db: Session = Depends(get_db),
    query_params: GetData = Depends()
):
    return controller.get_data(db, query_params)

@router.post("/crud")
def create_data(
    *,
    db: Session = Depends(get_db),
    query_params: CreateData,
):
    return controller.create_data(db, query_params)

@router.put("/crud")
def update_data(
    *,
    db: Session = Depends(get_db),
    query_params: UpdateData,
):
    return controller.update_data(db, query_params)

@router.delete("/crud")
def delete_data(
    *,
    db: Session = Depends(get_db),
    data_id: str
):
    return controller.delete_data(db, data_id)

