from checks.base_check import BaseCheck
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

REQUIRED_TITLES = [
    "СОДЕРЖАНИЕ", "ВВЕДЕНИЕ", "ЗАКЛЮЧЕНИЕ", "СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ"
]

class CenteredNoIndentCheck(BaseCheck):
    def run(self):
        for para in self.document.paragraphs:
            text = para.text.strip()
            for title in REQUIRED_TITLES:
                if text.lower() == title.lower():
                    alignment = para.paragraph_format.alignment or para.style.paragraph_format.alignment
                    if alignment != WD_PARAGRAPH_ALIGNMENT.CENTER:
                        para.runs[0].add_comment(
                            "Заголовок должен быть по центру.",
                            author="Проверка", initials="PR"
                        )
                    if para.paragraph_format.first_line_indent:
                        para.runs[0].add_comment(
                            "У заголовка не должно быть красной строки.",
                            author="Проверка", initials="PR"
                        )
