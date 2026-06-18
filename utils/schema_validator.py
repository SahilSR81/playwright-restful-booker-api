import json
from pathlib import Path

from jsonschema import validate


def validate_schema(response_data, schema_path):

    base_dir = Path(__file__).resolve().parents[1]
    schema_file = (base_dir / schema_path).resolve()

    with open(schema_file) as file:

        schema = json.load(file)

    validate(
        instance=response_data,
        schema=schema
    )