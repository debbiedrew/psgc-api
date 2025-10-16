from fastapi import APIRouter, HTTPException, Query
from core.service import (
    get_barangays_by_city_municipality,
    get_barangay_by_psgc,
)

router = APIRouter(prefix="/barangays", tags=["Barangays"])

@router.get("/", summary="Get all barangays under a city or municipality")
def list_barangays_by_city_municipality(
    city_mun_code: str = Query(..., description="City/Municipality PSGC 10-digit code")
):
    data = get_barangays_by_city_municipality(city_mun_code)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"No barangays found under city/municipality {city_mun_code}",
        )
    return data


@router.get("/{psgc_code}", summary="Get a specific barangay by PSGC 10-digit code")
def get_barangay(psgc_code: str):
    record = get_barangay_by_psgc(psgc_code)
    if not record:
        raise HTTPException(
            status_code=404,
            detail=f"Barangay not found for PSGC {psgc_code}",
        )
    return record
