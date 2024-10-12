from fastapi import APIRouter, Depends, Request

router = APIRouter()

@router.get("/crud")
def get_data(
):
    return "get data"

@router.post("/crud")
def create_data(
):
    return "create data"

@router.put("/crud")
def update_data(
):
    return "update data"

@router.delete("/crud")
def delete_data(
):
    return "delete data"

