import allure
from jsonschema import validate


@allure.step("Validate schema")
def validate_schema(instance, schema):
    validate(instance=instance, schema=schema)
