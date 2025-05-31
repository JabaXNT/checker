from .content_presence import ContentTitlePresenceCheck

class PresenceChecks:
    def get_checks(self):
        return [
            ContentTitlePresenceCheck
        ]
