from fastapi import APIRouter
from app.service import calculate_sum

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/sum")
def sum_numbers(a: int, b: int):
    result = calculate_sum(a, b)
    return {"result": result}