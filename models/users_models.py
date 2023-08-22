from dataclasses import dataclass

from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class Geo(JsonSchemaMixin):
    lat: str
    lng: str


@dataclass
class Address(JsonSchemaMixin):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


@dataclass
class Company(JsonSchemaMixin):
    name: str
    catchPhrase: str
    bs: str


@dataclass
class User(JsonSchemaMixin):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
