from enum import Enum


class TestResultSearchFiltersAssigneeIdsType1(str, Enum):
    ANY = "any"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
