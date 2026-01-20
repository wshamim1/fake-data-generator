import os
from typing import List

import pandas as pd

from fake_data_generator import FakeDataGenerator


class ExcelGenerator:
    def __init__(self, config_path: str = "config/columns.yaml") -> None:
        self.generator = FakeDataGenerator(config_path)

    def write(self, num_entries: int = 100, output_path: str = "data/fake_data.xlsx") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        records = self.generator.generate_records(num_entries)
        flat: List[dict] = [self.generator.flatten_record(r) for r in records]
        df = pd.DataFrame(flat)
        df.to_excel(output_path, index=False, engine="openpyxl")
        return output_path


def main() -> None:
    g = ExcelGenerator()
    path = g.write()
    print(f"Wrote Excel data to {path}")


if __name__ == "__main__":
    main()
