import json
import os
from typing import Any

from fake_data_generator import FakeDataGenerator


class JSONGenerator:
    def __init__(self, config_path: str = "config/columns.yaml") -> None:
        self.generator = FakeDataGenerator(config_path)

    def write(self, num_entries: int = 1000, output_path: str = "data/fake_data.json") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = self.generator.generate_records(num_entries)
        with open(output_path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
        return output_path


def main() -> None:
    g = JSONGenerator()
    path = g.write()
    print(f"Wrote JSON data to {path}")


if __name__ == "__main__":
    main()
