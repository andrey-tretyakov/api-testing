import enum


class APIPaths(enum.Enum):
    USERS = "/users"

    def __str__(self) -> str:
        return self.value
