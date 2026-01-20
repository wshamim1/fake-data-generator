import os
from typing import Any

import yaml

from fake_data_generator import FakeDataGenerator


class YAMLGenerator:
    def __init__(self, config_path: str = "config/columns.yaml") -> None:
        self.generator = FakeDataGenerator(config_path)

    def write(self, num_entries: int = 100, output_path: str = "data/fake_data.yaml") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        records = self.generator.generate_records(num_entries)
        with open(output_path, "w", encoding="utf-8") as fh:
            yaml.safe_dump(records, fh, sort_keys=False, allow_unicode=True)
        return output_path


def main() -> None:
    g = YAMLGenerator()
    path = g.write()
    print(f"Wrote YAML data to {path}")


if __name__ == "__main__":
    main()
