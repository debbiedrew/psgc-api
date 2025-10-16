from fastapi import APIRouter, HTTPException, Query
from core.service import (
    get_cities_municipalities_by_province,
    get_city_municipality_by_psgc,
)

router = APIRouter(prefix="/cities-municipalities", tags=["Cities & Municipalities"])

@router.get("/", summary="Get all cities and municipalities under a province")
def list_cities_municipalities_by_province(
    province_code: str = Query(..., description="Province PSGC 10-digit code")
):
    data = get_cities_municipalities_by_province(province_code)
    if not data:
        raise HTTPException(status_code=404, detail=f"No cities/municipalities found under province {province_code}")
    return data

@router.get("/{psgc_code}", summary="Get a specific city or municipality by PSGC 10-digit code")
def get_city_or_municipality(psgc_code: str):
    record = get_city_municipality_by_psgc(psgc_code)
    if not record:
        raise HTTPException(status_code=404, detail=f"City or municipality not found for PSGC {psgc_code}")
    return record
