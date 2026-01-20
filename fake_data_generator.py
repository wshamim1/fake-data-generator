import os
from typing import Any, Dict, List

import yaml
from faker import Faker


class FakeDataGenerator:
    """Load column providers from a YAML config and generate fake records."""

    def __init__(self, config_path: str = "config/columns.yaml", seed: int | None = None):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config not found: {config_path}")

        with open(config_path, "r", encoding="utf-8") as fh:
            self.config = yaml.safe_load(fh)

        self.columns = self.config.get("columns", [])
        self.fake = Faker()
        if seed is not None:
            self.fake.seed_instance(seed)

    def _call_provider(self, provider: Any) -> Any:
        # provider can be a string method name or a nested dict
        if isinstance(provider, str):
            func = getattr(self.fake, provider)
            return func()
        if isinstance(provider, dict):
            return {k: self._call_provider(v) for k, v in provider.items()}
        return None

    def _apply_transforms(self, value: Any, col_conf: Dict[str, Any]) -> Any:
        if isinstance(value, str) and col_conf.get("replace_newlines"):
            value = value.replace("\n", ", ")
        if col_conf.get("as_iso") and hasattr(value, "isoformat"):
            value = value.isoformat()
        return value

    def generate_record(self) -> Dict[str, Any]:
        record: Dict[str, Any] = {}
        for col in self.columns:
            name = col["name"]
            provider = col["provider"]
            value = self._call_provider(provider)
            value = self._apply_transforms(value, col)
            record[name] = value
        return record

    def generate_records(self, n: int) -> List[Dict[str, Any]]:
        return [self.generate_record() for _ in range(n)]

    @staticmethod
    def flatten_record(record: Dict[str, Any]) -> Dict[str, Any]:
        flat: Dict[str, Any] = {}
        for k, v in record.items():
            if isinstance(v, dict):
                for subk, subv in v.items():
                    flat[f"{k}_{subk}"] = subv
            else:
                flat[k] = v
        return flat
