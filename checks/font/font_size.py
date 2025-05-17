import re
from base_check import BaseCheck
from docx.shared import Pt

class FontSizeCheck(BaseCheck):
    REQUIRED_SIZE_PT = 14
    # Регекс для подпунктов формата "1.1", "1.1.1", "2.3.4.5" и т.п.
    SUBPOINT_REGEX = re.compile(r'^\d+(\.\d+)+\s')

    def get_effective_font_size(self, run, para):
        # Игнорируем runs без текста
        if not run.text.strip():
            return None

        # Проверяем локальный размер шрифта в run
        if run.font and run.font.size:
            return run.font.size.pt

        # Проверяем размер шрифта в стиле run (если он есть)
        if hasattr(run, 'style') and run.style and hasattr(run.style, 'font') and run.style.font and run.style.font.size:
            return run.style.font.size.pt

        # Проверяем размер шрифта в стиле параграфа
        if para.style and hasattr(para.style, 'font') and para.style.font and para.style.font.size:
            return para.style.font.size.pt

        return None

    def run(self):
        for para in self.document.paragraphs:
            # Пропускаем списки по имени стиля
            if para.style and para.style.name and "List" in para.style.name:
                continue  # пропускаем параграфы списков

            # Пропускаем подпункты вида 1.1, 1.1.1, 2.3.4.5 и т.п.
            if self.SUBPOINT_REGEX.match(para.text.strip()):
                continue

            for run in para.runs:
                size_pt = self.get_effective_font_size(run, para)
                if size_pt is None:
                    # Пропускаем пустые run без текста
                    if run.text.strip():
                        run.add_comment(
                            f"Размер шрифта не задан явно, должен быть {self.REQUIRED_SIZE_PT} пт",
                            author="Проверка", initials="PR"
                        )
                elif abs(size_pt - self.REQUIRED_SIZE_PT) > 0.1:
                    run.add_comment(
                        f"Размер шрифта должен быть {self.REQUIRED_SIZE_PT} пт, найден {size_pt:.1f} пт",
                        author="Проверка", initials="PR"
                    )
