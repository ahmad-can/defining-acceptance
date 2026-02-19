from enum import Enum


class Permission(str, Enum):
    ADD_APPLICATION = "add_application"
    CHANGE_APPLICATION = "change_application"
    CHANGE_ARTEFACT = "change_artefact"
    CHANGE_ATTACHMENT_RULE = "change_attachment_rule"
    CHANGE_ENVIRONMENT_REPORTED_ISSUE = "change_environment_reported_issue"
    CHANGE_ENVIRONMENT_REVIEW = "change_environment_review"
    CHANGE_ISSUE = "change_issue"
    CHANGE_ISSUE_ATTACHMENT = "change_issue_attachment"
    CHANGE_ISSUE_ATTACHMENT_BULK = "change_issue_attachment_bulk"
    CHANGE_RERUN = "change_rerun"
    CHANGE_RERUN_BULK = "change_rerun_bulk"
    CHANGE_TEAM = "change_team"
    CHANGE_TEST = "change_test"
    CHANGE_TEST_CASE_REPORTED_ISSUE = "change_test_case_reported_issue"
    CHANGE_USER = "change_user"
    VIEW_APPLICATION = "view_application"
    VIEW_ARTEFACT = "view_artefact"
    VIEW_ENVIRONMENT_REPORTED_ISSUE = "view_environment_reported_issue"
    VIEW_ENVIRONMENT_REVIEW = "view_environment_review"
    VIEW_ISSUE = "view_issue"
    VIEW_PERMISSION = "view_permission"
    VIEW_REPORT = "view_report"
    VIEW_RERUN = "view_rerun"
    VIEW_TEAM = "view_team"
    VIEW_TEST = "view_test"
    VIEW_TEST_CASE_REPORTED_ISSUE = "view_test_case_reported_issue"
    VIEW_USER = "view_user"

    def __str__(self) -> str:
        return str(self.value)
