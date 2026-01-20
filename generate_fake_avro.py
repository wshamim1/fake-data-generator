import os
from typing import List

from fastavro import writer, parse_schema

from fake_data_generator import FakeDataGenerator


def _build_schema() -> dict:
    return {
        "doc": "Fake people schema",
        "name": "Person",
        "type": "record",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "address", "type": "string"},
            {"name": "email", "type": "string"},
            {"name": "phone_number", "type": "string"},
            {"name": "job", "type": "string"},
            {"name": "company", "type": "string"},
            {"name": "birthdate", "type": "string"},
            {
                "name": "credit_card",
                "type": {
                    "name": "CreditCard",
                    "type": "record",
                    "fields": [
                        {"name": "number", "type": "string"},
                        {"name": "provider", "type": "string"},
                        {"name": "expiration_date", "type": "string"},
                    ],
                },
            },
            {"name": "ssn", "type": "string"},
        ],
    }


class AvroGenerator:
    def __init__(self, config_path: str = "config/columns.yaml") -> None:
        self.generator = FakeDataGenerator(config_path)
        self.schema = parse_schema(_build_schema())

    def write(self, num_entries: int = 100, output_path: str = "data/fake_data.avro") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        records: List[dict] = self.generator.generate_records(num_entries)
        # fastavro expects nested dicts to match the schema
        with open(output_path, "wb") as fh:
            writer(fh, self.schema, records)
        return output_path


def main() -> None:
    g = AvroGenerator()
    path = g.write()
    print(f"Wrote Avro data to {path}")


if __name__ == "__main__":
    main()
