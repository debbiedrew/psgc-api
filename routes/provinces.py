from fastapi import APIRouter, HTTPException, Query
from core.service import get_provinces, get_provinces_by_region

router = APIRouter(prefix="/provinces", tags=["Provinces"])

@router.get("/", summary="Get provinces filtered by region")
def list_provinces(region_code: str = Query(None, description="Optional region PSGC code")):
    if region_code:
        provinces = get_provinces_by_region(region_code)
        if not provinces:
            raise HTTPException(status_code=404, detail=f"No provinces found under region PSGC {region_code}")
        return provinces
    return get_provinces()

@router.get("/{psgc_code}", summary="Get province by PSGC 10-digit code")
def get_province_by_code(psgc_code: str):
    provinces = get_provinces()
    for province in provinces:
        if province.get("psgc10DigitCode") == psgc_code:
            return province
    raise HTTPException(status_code=404, detail="Province not found")
