import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import Dict, Any

from fake_data_generator import FakeDataGenerator


class XMLGenerator:
    def __init__(self, config_path: str = "config/columns.yaml") -> None:
        self.generator = FakeDataGenerator(config_path)

    def _dict_to_element(self, parent: ET.Element, data: Dict[str, Any]) -> None:
        for k, v in data.items():
            if isinstance(v, dict):
                child = ET.SubElement(parent, k)
                self._dict_to_element(child, v)
            else:
                ET.SubElement(parent, k).text = str(v)

    def pretty_print_xml(self, element: ET.Element) -> str:
        rough = ET.tostring(element, "utf-8")
        parsed = minidom.parseString(rough)
        return parsed.toprettyxml(indent="  ")

    def write(self, num_people: int = 20, output_path: str = "data/fake_people_catalog.xml") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        root = ET.Element("people_catalog")
        records = self.generator.generate_records(num_people)
        for rec in records:
            person = ET.SubElement(root, "person")
            self._dict_to_element(person, rec)

        xml_string = self.pretty_print_xml(root)
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(xml_string)

        return output_path


def main() -> None:
    g = XMLGenerator()
    path = g.write()
    print(f"Wrote XML catalog to {path}")


if __name__ == "__main__":
    main()
