from base_check import BaseCheck

class FontNameCheck(BaseCheck):
    REQUIRED_FONT = "Times New Roman"

    def run(self):
        for para in self.document.paragraphs:
            for run in para.runs:
                font_name = run.font.name
                if font_name and font_name.lower() != self.REQUIRED_FONT.lower():
                    run.add_comment(
                        f"Шрифт должен быть {self.REQUIRED_FONT}, а найден: {font_name}",
                        author="Проверка", initials="PR"
                    )