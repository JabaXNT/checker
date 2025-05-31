from .uppercase_title import UppercaseTitleCheck
from .bold_title import BoldTitleCheck
from .centered_no_indent import CenteredNoIndentCheck
from .spacing_after_title import SpacingAfterTitleCheck
from .new_page_check import NewPageCheck

class StructureChecks:
    def get_checks(self):
        return [
            UppercaseTitleCheck,
            BoldTitleCheck,
            CenteredNoIndentCheck,
            SpacingAfterTitleCheck,
            NewPageCheck
        ]
