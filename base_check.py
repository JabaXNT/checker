from docx.document import Document as DocxDocument

class BaseCheck:
    def __init__(self, document: DocxDocument):
        self.document = document

    def run(self):
        """
        Выполняет проверку и вносит необходимые комментарии в документ.
        """
        raise NotImplementedError("Метод run должен быть реализован в подклассе")
