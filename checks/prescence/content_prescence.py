from base_check import BaseCheck

class ContentTitlePresenceCheck(BaseCheck):
    CONTENT_TITLE = "СОДЕРЖАНИЕ"

    def run(self):
        found = any(para.text.strip().upper() == self.CONTENT_TITLE for para in self.document.paragraphs)

        if not found:
            # Добавляем комментарий к первому параграфу
            if self.document.paragraphs:
                self.document.paragraphs[0].runs[0].add_comment(
                    "Заголовок 'СОДЕРЖАНИЕ' не найден в документе (включая таблицы).",
                    author="Проверка", initials="PR"
                )

# содержание не находится, если оно есть в таблице, а не отдельным параграфом