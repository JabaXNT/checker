from checks.base_check import BaseCheck

REQUIRED_TITLES = [
    "СОДЕРЖАНИЕ", "ВВЕДЕНИЕ", "ЗАКЛЮЧЕНИЕ", "СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ"
]

class BoldTitleCheck(BaseCheck):
    def is_paragraph_bold(self, paragraph):
        """
        Возвращает True, если весь параграф визуально жирный.
        """
        has_text = False
        for run in paragraph.runs:
            if run.text.strip():
                has_text = True
                # run.bold = True — явно установлено
                # run.bold = None — надо проверить стиль
                if not (run.bold is True or (
                    run.bold is None and hasattr(run.style, "font") and run.style.font.bold
                )):
                    return False
        return has_text


    def run(self):
        for para in self.document.paragraphs:
            text = para.text.strip()
            for title in REQUIRED_TITLES:
                if text.lower() == title.lower():
                    if not self.is_paragraph_bold(para):
                        para.runs[0].add_comment(
                            "Заголовок должен быть полужирным.",
                            author="Проверка", initials="PR"
                        )
