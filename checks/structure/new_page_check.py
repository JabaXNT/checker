from checks.base_check import BaseCheck

REQUIRED_TITLES = [
    "СОДЕРЖАНИЕ", "ВВЕДЕНИЕ", "ЗАКЛЮЧЕНИЕ", "СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ"
]

class NewPageCheck(BaseCheck):
    def has_manual_page_break(self, para_idx):
        """Проверка: есть ли разрыв страницы в предыдущих параграфах"""
        for idx in range(para_idx - 1, -1, -1):
            prev_para = self.document.paragraphs[idx]
            for run in prev_para.runs:
                if '\f' in run.text:
                    return True
            if prev_para.text.strip():
                break
        return False

    def has_spacing_heuristic(self, para_idx, empty_required=2):
        """Эвристика: есть ли перед заголовком несколько пустых строк"""
        empty_count = 0
        for idx in range(para_idx -1, -1, -1):
            prev_para = self.document.paragraphs[idx]
            if not prev_para.text.strip():
                empty_count += 1
            else:
                break
            if empty_count >= empty_required:
                return True
        return False

    def starts_on_new_page(self, para_idx):
        return self.has_manual_page_break(para_idx) or self.has_spacing_heuristic(para_idx)

    def run(self):
        for idx, para in enumerate(self.document.paragraphs):
            text = para.text.strip()
            for title in REQUIRED_TITLES:
                if text.upper() == title:
                    if not self.starts_on_new_page(idx):
                        if para.runs:
                            para.runs[0].add_comment(
                                "Заголовок должен начинаться с новой страницы. Добавьте разрыв страницы (Ctrl + Enter) или проверьте структуру документа.",
                                author="Проверка",
                                initials="PR"
                            )
