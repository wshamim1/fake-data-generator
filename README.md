# fake-data-generator

This repository provides small utilities to generate fake datasets (CSV, JSON, Parquet, XML) using Faker.

Files (refactored):

- `generate_fake_csv.py` — write CSV data to `data/fake_data.csv`
- `generate_fake_json.py` — write JSON data to `data/fake_data.json`
- `generate_fake_parquet.py` — write Parquet data to `data/fake_data.parquet` (requires `pyarrow`)
- `generate_fake_xml.py` — write XML catalog to `data/fake_people_catalog.xml`
- `generate_fake_yaml.py` — write YAML data to `data/fake_data.yaml` (requires `pyyaml`)
- `generate_fake_excel.py` — write Excel data to `data/fake_data.xlsx` (requires `openpyxl`)
- `generate_fake_tsv.py` — write TSV data to `data/fake_data.tsv`
- `generate_fake_avro.py` — write Avro data to `data/fake_data.avro` (requires `fastavro`)
- `generate_fake_sql.py` — write SQL file with CREATE/INSERT statements to `data/fake_data.sql`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run an example:

```bash
python generate_fake_csv.py
python generate_fake_json.py
python generate_fake_parquet.py
python generate_fake_xml.py
python generate_fake_yaml.py
python generate_fake_excel.py
python generate_fake_tsv.py
```
