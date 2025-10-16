import json
import os
from functools import lru_cache

JSON_PATH = "./generatedData/psgc.json"

@lru_cache(maxsize=1)
def load_psgc_data():
    if not os.path.exists(JSON_PATH):
        raise FileNotFoundError(f"File not found: {JSON_PATH}")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def safe_level_match(record, level):
    """Check geographic level safely (avoid NoneType)."""
    return (
        isinstance(record.get("geographicLevel"), str)
        and record["geographicLevel"].strip().lower() == level
    )
