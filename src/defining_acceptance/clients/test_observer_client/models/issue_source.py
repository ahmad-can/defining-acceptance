from enum import Enum


class IssueSource(str, Enum):
    GITHUB = "github"
    JIRA = "jira"
    LAUNCHPAD = "launchpad"

    def __str__(self) -> str:
        return str(self.value)
