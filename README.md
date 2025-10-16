PSGC API — FastAPI Implementation

A fully modular FastAPI-based API for browsing the Philippine Standard Geographic Code (PSGC) dataset.
This project reads data from a psgc.json (converted from PSGC Publication Excel File) and serves structured geographic data such as:

Regions
Provinces (including Metro Manila)
Cities / Municipalities
Barangays


psgc-api
├── core
│   ├── generateJson.py             # Generate json file from PSGC Publication
│   ├── service.py                  # Core logic and cached data loader
│   └── utils.py
├── generatedData
│   └── psgc.json
├── publicationFiles
│   └── your_csv_file.csv           # PSGC Publication
├── routes
│   ├── barangays.py                # /barangays endpoints
│   ├── citiesMunicipalities.py     # /cities-municipalities endpoints
│   ├── provinces.py                # /provinces endpoints
│   └── regions.py                  # /regions endpoints
├── .gitignore
├── app.py
├── README.md
└── requirements.txt