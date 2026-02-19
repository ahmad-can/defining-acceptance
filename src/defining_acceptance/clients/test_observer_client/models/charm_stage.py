from enum import Enum


class CharmStage(str, Enum):
    BETA = "beta"
    CANDIDATE = "candidate"
    EDGE = "edge"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
