from fastapi import FastAPI
from routes import citiesMunicipalities, regions, provinces, barangays

app = FastAPI(
    title="PSGC API - Regions, Provinces, Cities, Municipalities, and Barangays",
    version="2.1",
    description="This project uses the Philippine Standard Geographic Code (PSGC) dataset, current as of October 13, 2025. Reference: https://psa.gov.ph/classification/psgc/",
)

# Include Routers
app.include_router(regions.router)
app.include_router(provinces.router)
app.include_router(citiesMunicipalities.router)
app.include_router(barangays.router)
