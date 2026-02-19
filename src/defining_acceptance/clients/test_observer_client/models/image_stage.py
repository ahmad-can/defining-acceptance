from enum import Enum


class ImageStage(str, Enum):
    CURRENT = "current"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
