from io import BytesIO
from docx import Document
from orchestrator import CheckOrchestrator
from checks.structure import StructureChecks
from checks.presence import PresenceChecks
from checks.font import FontChecks


def run_checks_file(input_path: str, output_path: str):
    # Загрузка DOCX
    doc = Document(input_path)

    # Инициализация оркестратора с группами проверок
    orchestrator = CheckOrchestrator([
        StructureChecks(),
        PresenceChecks(),
        FontChecks(),
    ])

    # Запуск всех проверок
    orchestrator.run(doc)

    # Сохранение результата
    doc.save(output_path)


if __name__ == "__main__":
    run_checks_file(
        "2_Ваганов_В_С_РИ_400022_Пояснительная_записка_ВКР_—_копия.docx",
        "Checked_Output.docx"
    )
