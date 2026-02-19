from enum import Enum


class IssueStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
