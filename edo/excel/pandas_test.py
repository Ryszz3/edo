from os.path import exists

import pandas as pd
import os
from edo.settings import BASE_DIR
path = BASE_DIR / "uploads" / "excel"
df = pd.DataFrame()

def extract_sheets():
    for file in os.listdir(BASE_DIR / "uploads" / "excel"):
        if file.endswith(".xlsx"):
            xlfile = pd.ExcelFile(path / file)
            sheets = xlfile.sheet_names
            sheets_path = path / f'{file.split(".")[0]}_sheets'
            os.makedirs(sheets_path, exist_ok=True)

            for sheet in sheets:
                name = f'{file.split(".")[0]}_{sheet}'
                output_file = sheets_path / f'{name}.xlsx'
                print(path / name)
                print(name)
                data = xlfile.parse(sheet)
                data.to_excel(output_file, sheet_name=name, index=False, header=False)



