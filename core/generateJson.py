import pandas as pd
from pathlib import Path
import json

class PSGCConverter:
    def __init__(self, csv_file_path, output_file_path):
        self.csv_file_path = Path(csv_file_path)
        self.output_file_path = Path(output_file_path)

        self.headers = [
            "psgc10DigitCode",
            "name",
            "code",
            "geographicLevel",
            "oldName",
            "cityClass",
            "incomeClassification",
            "urbanRural",
            "population2015",
            "emptyField",
            "population2020",
        ]

        self.omit_fields = [
            "population2015",
            "emptyField",
            "population2020",
            "field12",
        ]

    def read_csv(self):
        print(f"Reading CSV file: {self.csv_file_path}")
        df = pd.read_csv(self.csv_file_path, names=self.headers, header=None, encoding="utf-8")
        return df

    def clean_data(self, df):
        print("Cleaning data (removing unwanted fields)...")
        return df.drop(columns=[c for c in self.omit_fields if c in df.columns])

    def add_metro_manila(self, df):
        """Add Metro Manila as a province if not present."""

        metro_psgc = "1300000000"
        print("Adding Metro Manila (1300000000) as a province...")

        new_row = {
            "psgc10DigitCode": metro_psgc,
            "name": "Metro Manila",
            "code": "",
            "geographicLevel": "Prov",
            "oldName": "",
            "cityClass": "",
            "incomeClassification": "",
            "urbanRural": "",
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        return df

    def fix_isabel(self, df):
        """If PSGC 0990100000 exists, make it a province named 'Isabela'."""
        
        target_psgc = "0990100000"
        if (df["psgc10DigitCode"] == target_psgc).any():
            print("Fixing PSGC 0990100000 → setting as province 'Isabela'...")
            df.loc[df["psgc10DigitCode"] == target_psgc, "geographicLevel"] = "Prov"
            df.loc[df["psgc10DigitCode"] == target_psgc, "name"] = "Isabela"
        else:
            print("PSGC 0990100000 not found in dataset — no fix needed.")
        return df

    def save_json(self, df):
        print(f"Saving to file: {self.output_file_path}")
        json_str = df.to_json(orient="records", force_ascii=False, indent=2)
        self.output_file_path.write_text(json_str, encoding="utf-8")

    def convert(self):
        df = self.read_csv()
        df_clean = self.clean_data(df)
        df_with_metro = self.add_metro_manila(df_clean)
        df_final = self.fix_isabel(df_with_metro)
        self.save_json(df_final)
        print("Done.")

""" Modify the csv file path to your file"""
if __name__ == "__main__":
    converter = PSGCConverter(
        csv_file_path="./publicationFiles/3Q_2025_psgc.csv",
        output_file_path="./psgc.json"
    )
    converter.convert()
