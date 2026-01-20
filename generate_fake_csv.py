import csv
import os
from typing import Dict

from fake_data_generator import FakeDataGenerator


class CSVGenerator:
    def __init__(self, config_path: str = "config/columns.yaml") -> None:
        self.generator = FakeDataGenerator(config_path)

    def write(self, num_entries: int = 100, output_path: str = "data/fake_data.csv") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        records = self.generator.generate_records(num_entries)
        flat = [self.generator.flatten_record(r) for r in records]
        headers = list(flat[0].keys()) if flat else []

        with open(output_path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=headers)
            writer.writeheader()
            writer.writerows(flat)

        return output_path


def main() -> None:
    g = CSVGenerator()
    path = g.write()
    print(f"Wrote CSV data to {path}")


if __name__ == "__main__":
    main()
