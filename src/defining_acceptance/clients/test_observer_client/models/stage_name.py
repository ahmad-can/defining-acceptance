from enum import Enum


class StageName(str, Enum):
    BETA = "beta"
    CANDIDATE = "candidate"
    CURRENT = "current"
    EDGE = "edge"
    PENDING = "pending"
    PROPOSED = "proposed"
    STABLE = "stable"
    UPDATES = "updates"

    def __str__(self) -> str:
        return str(self.value)
