"""Read filtered site records and write Frappe-compatible fixture JSON to this repo."""

import json
import os
import re
import shutil
import tempfile
from pathlib import Path

import frappe
from frappe.core.doctype.data_import.data_import import export_json

from property_manager.hooks import fixtures


SENSITIVE = re.compile(r"password|secret|token|api_key", re.IGNORECASE)
IMPORT_FIRST = {
    "DocType": "00_doctype.json",
    "Role": "01_role.json",
    "Custom Field": "02_custom_field.json",
    "Custom DocPerm": "03_custom_docperm.json",
}


def run():
    repo = Path(os.environ["PROPERTY_MANAGER_REPO"]).resolve()
    destination = repo / "property_manager" / "fixtures"
    if not (repo / "property_manager" / "hooks.py").is_file():
        raise RuntimeError("PROPERTY_MANAGER_REPO must point to the property_manager checkout")

    # Frappe's exporter removes the same metadata as bench export-fixtures.
    # Stage every result so a failed secret check never alters the checkout.
    with tempfile.TemporaryDirectory(prefix="property-fixtures-") as tmp:
        staged = []
        for fixture in fixtures:
            doctype = fixture["dt"]
            if doctype == "Email Account":
                raise RuntimeError("Email Account must never be exported")
            path = Path(tmp) / IMPORT_FIRST.get(doctype, frappe.scrub(doctype) + ".json")
            export_json(
                doctype,
                str(path),
                filters=fixture.get("filters"),
                or_filters=fixture.get("or_filters"),
                order_by="name asc",
            )
            content = path.read_text(encoding="utf-8")
            if SENSITIVE.search(content):
                raise RuntimeError(f"Sensitive term found in staged {path.name}; no fixtures were changed")
            count = len(json.loads(content))
            staged.append((path, destination / path.name, doctype, count))

        destination.mkdir(parents=True, exist_ok=True)
        for source, target, doctype, count in staged:
            with tempfile.NamedTemporaryFile(dir=destination, delete=False) as output:
                temporary_target = Path(output.name)
            try:
                shutil.copyfile(source, temporary_target)
                os.replace(temporary_target, target)
            finally:
                temporary_target.unlink(missing_ok=True)
            print(f"{doctype}: {count}")
