from checks.base_check import BaseCheck

REQUIRED_TITLES = [
    "СОДЕРЖАНИЕ", "ВВЕДЕНИЕ", "ЗАКЛЮЧЕНИЕ", "СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ"
]

class SpacingAfterTitleCheck(BaseCheck):
    def run(self):
        paragraphs = self.document.paragraphs
        for i, para in enumerate(paragraphs[:-1]):
            text = para.text.strip()
            next_text = paragraphs[i + 1].text.strip()
            for title in REQUIRED_TITLES:
                if text.lower() == title.lower():
                    if next_text != "":
                        para.runs[0].add_comment(
                            "После заголовка должна быть одна пустая строка.",
                            author="Проверка", initials="PR"
                        )
