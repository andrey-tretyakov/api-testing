from dataclasses import dataclass

from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class Post(JsonSchemaMixin):
    userId: int
    id: int
    title: str
    body: str


@dataclass
class PostRequest(JsonSchemaMixin):
    userId: int
    title: str
    body: str
