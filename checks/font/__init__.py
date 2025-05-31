from .font_check import FontNameCheck
from .font_size import FontSizeCheck

class FontChecks:
    def get_checks(self):
        return [
            FontSizeCheck,
            FontNameCheck
        ]
