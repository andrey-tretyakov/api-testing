import enum


class APIParams(enum.Enum):
    USER_ID = "userId"

    def __str__(self) -> str:
        return self.value
