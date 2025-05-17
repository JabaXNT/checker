from docx import Document

from checks.structure.uppercase_title import UppercaseTitleCheck
from checks.structure.centered_no_indent import CenteredNoIndentCheck
from checks.structure.bold_title import BoldTitleCheck
from checks.structure.spacing_after_title import SpacingAfterTitleCheck
from checks.structure.new_page_check import NewPageCheck
from checks.prescence.content_prescence import ContentTitlePresenceCheck
from checks.font.font_check import FontNameCheck
from checks.font.font_size import FontSizeCheck

CHECK_CLASSES = [
    UppercaseTitleCheck,
    CenteredNoIndentCheck,
    BoldTitleCheck,
    SpacingAfterTitleCheck,
    NewPageCheck,
    ContentTitlePresenceCheck,
    FontNameCheck,
    FontSizeCheck
]

def run_checks_doc(doc: Document) -> Document:
    for CheckClass in CHECK_CLASSES:
        check = CheckClass(doc)
        check.run()
    return doc

def run_checks_file(input_path: str, output_path: str):
    doc = Document(input_path)
    checked_doc = run_checks_doc(doc)
    checked_doc.save(output_path)

if __name__ == "__main__":
    run_checks_file(
        "2_Ваганов_В_С_РИ_400022_Пояснительная_записка_ВКР_—_копия.docx",
        "Checked_Output.docx"
    )