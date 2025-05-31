from checks.base_check import BaseCheck
from docx import Document

REQUIRED_TITLES = [
    "СОДЕРЖАНИЕ",
    "ВВЕДЕНИЕ",
    "ЗАКЛЮЧЕНИЕ",
    "СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ"
]

class UppercaseTitleCheck(BaseCheck):
    def run(self):
        for para in self.document.paragraphs:
            para_text = para.text.strip()
            for required_title in REQUIRED_TITLES:
                if para_text.lower() == required_title.lower():
                    if para_text != para_text.upper():
                        if para.runs:
                            para.runs[0].add_comment(
                                f"Заголовок «{para_text}» должен быть написан ЗАГЛАВНЫМИ буквами.",
                                author="Проверка",
                                initials="PR"
                            )
