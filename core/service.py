from .utils import load_psgc_data, safe_level_match

def get_regions():
    data = load_psgc_data()
    return [d for d in data if safe_level_match(d, "reg")]

def get_provinces():
    data = load_psgc_data()
    provinces = [d for d in data if safe_level_match(d, "prov")]

    # Add Metro Manila manually if not present
    if not any(p.get("psgc10DigitCode") == "1300000000" for p in provinces):
        provinces.append({
            "psgc10DigitCode": "1300000000",
            "name": "Metro Manila",
            "code": "13",
            "geographicLevel": "prov",
        })
    return provinces

def get_provinces_by_region(region_psgc: str):
    provinces = get_provinces()
    region_prefix = region_psgc[:2]
    filtered = [p for p in provinces if p.get("psgc10DigitCode", "").startswith(region_prefix)]

    if region_prefix == "13" and not any(p["name"] == "Metro Manila" for p in filtered):
        filtered.append({
            "psgc10DigitCode": "1300000000",
            "name": "Metro Manila",
            "code": "13",
            "geographicLevel": "prov",
        })
    return filtered

def get_cities_municipalities():
    data = load_psgc_data()
    return [
        d for d in data
        if safe_level_match(d, "mun") or safe_level_match(d, "city")
    ]

def get_cities_municipalities_by_province(province_psgc: str):
    """Return cities/municipalities filtered by province PSGC code."""
    cities_muns = get_cities_municipalities()

    # Metro Manila special case — match by region code (13)
    if province_psgc == "1300000000":
        return [
            d for d in cities_muns
            if d.get("psgc10DigitCode", "").startswith("13")
        ]
    
    province_segment = province_psgc[2:5]
    return [
        d for d in cities_muns
        if d.get("psgc10DigitCode", "")[2:5] == province_segment
    ]

def get_city_municipality_by_psgc(psgc_code: str):
    cities_muns = get_cities_municipalities()
    for item in cities_muns:
        if item.get("psgc10DigitCode") == psgc_code:
            return item
    return None

def get_barangays():
    """Return all barangays."""
    data = load_psgc_data()
    return [d for d in data if safe_level_match(d, "bgy")]

# def get_barangays_by_city_municipality(city_mun_psgc: str):
#     """Return barangays filtered by their city/municipality PSGC code."""
#     barangays = get_barangays()
#     prefix = city_mun_psgc[:6]
#     return [b for b in barangays if b.get("psgc10DigitCode", "").startswith(prefix)]

def get_barangays_by_city_municipality(city_mun_psgc: str):
    """Return barangays filtered by their city/municipality PSGC code.

    - Matches barangays whose PSGC code shares the same 3rd to 7th digits
      as the provided city/municipality PSGC.
    """
    barangays = get_barangays()
    city_segment = city_mun_psgc[2:7]  # Extract digits 3–7
    return [
        b for b in barangays
        if b.get("psgc10DigitCode", "")[2:7] == city_segment
    ]
def get_barangay_by_psgc(psgc_code: str):
    """Return a single barangay by exact PSGC 10-digit code."""
    barangays = get_barangays()
    for item in barangays:
        if item.get("psgc10DigitCode") == psgc_code:
            return item
    return None