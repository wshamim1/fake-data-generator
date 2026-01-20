import os
from typing import List

from fake_data_generator import FakeDataGenerator


def _escape_sql(value: object) -> str:
    if value is None:
        return "NULL"
    s = str(value)
    return "'" + s.replace("'", "''") + "'"


class SQLGenerator:
    def __init__(self, config_path: str = "config/columns.yaml", table_name: str = "fake_data") -> None:
        self.generator = FakeDataGenerator(config_path)
        self.table_name = table_name

    def write(self, num_entries: int = 100, output_path: str = "data/fake_data.sql") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        records: List[dict] = self.generator.generate_records(num_entries)
        flat = [self.generator.flatten_record(r) for r in records]

        with open(output_path, "w", encoding="utf-8") as fh:
            if not flat:
                fh.write("-- No data generated\n")
                return output_path

            cols = list(flat[0].keys())
            # Create table statement (all text columns)
            cols_def = ", ".join([f"{c} TEXT" for c in cols])
            fh.write(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({cols_def});\n\n")

            for row in flat:
                values = ", ".join([_escape_sql(row.get(c)) for c in cols])
                fh.write(f"INSERT INTO {self.table_name} ({', '.join(cols)}) VALUES ({values});\n")

        return output_path


def main() -> None:
    g = SQLGenerator()
    path = g.write()
    print(f"Wrote SQL data to {path}")


if __name__ == "__main__":
    main()
