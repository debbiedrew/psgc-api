from fastapi import APIRouter, HTTPException
from core.service import get_regions

router = APIRouter(prefix="/regions", tags=["Regions"])

@router.get("/", summary="Get all regions")
def list_regions():
    regions = get_regions()
    if not regions:
        raise HTTPException(status_code=404, detail="No regions found")
    return regions

@router.get("/{psgc_code}", summary="Get region by PSGC 10-digit code")
def get_region_by_code(psgc_code: str):
    regions = get_regions()
    for region in regions:
        if region.get("psgc10DigitCode") == psgc_code:
            return region
    raise HTTPException(status_code=404, detail="Region not found")
