# fake-data-generator

This repository provides small utilities to generate fake datasets (CSV, JSON, Parquet, XML) using Faker.

Get the code
--------

Clone this repository locally:

```bash
git clone https://github.com/WshamimGit/fake-data-generator.git
cd fake-data-generator
```

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

Setup and install
-----------------

It's recommended to create an isolated virtual environment before installing dependencies.

macOS / Linux (bash/zsh):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you use `pyenv` to manage Python versions, ensure the desired Python is selected before creating the venv (for example `pyenv shell 3.11.9`).


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
