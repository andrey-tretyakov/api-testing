import enum


class APIPaths(enum.Enum):
    USERS = "/users"
    POSTS = "/posts"

    def __str__(self) -> str:
        return self.value
