from docx import Document

class CheckOrchestrator:
    def __init__(self, check_groups):
        self.check_groups = check_groups

    def run(self, doc: Document):
        for group in self.check_groups:
            checks = group.get_checks()
            for CheckClass in checks:
                check = CheckClass(doc)
                check.run()
