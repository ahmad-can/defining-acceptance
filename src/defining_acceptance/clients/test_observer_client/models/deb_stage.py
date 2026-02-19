from enum import Enum


class DebStage(str, Enum):
    PROPOSED = "proposed"
    UPDATES = "updates"

    def __str__(self) -> str:
        return str(self.value)
