import os
from typing import List

import pandas as pd

from fake_data_generator import FakeDataGenerator


class ParquetGenerator:
    def __init__(self, config_path: str = "config/columns.yaml") -> None:
        self.generator = FakeDataGenerator(config_path)

    def write(self, num_entries: int = 1000, output_path: str = "data/fake_data.parquet") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        records = self.generator.generate_records(num_entries)
        flat: List[dict] = [self.generator.flatten_record(r) for r in records]
        df = pd.DataFrame(flat)
        df.to_parquet(output_path, index=False)
        return output_path


def main() -> None:
    g = ParquetGenerator()
    path = g.write()
    print(f"Wrote Parquet data to {path}")


if __name__ == "__main__":
    main()
