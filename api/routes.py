from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from docx import Document
from orchestrator import CheckOrchestrator
from checks.structure import StructureChecks
from checks.presence import PresenceChecks
from checks.font import FontChecks
from io import BytesIO

router = APIRouter()

@router.post("/check", summary="Upload .docx and get checked version")
async def check_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".docx"):
        return {"error": "Only .docx files are supported."}

    # Загружаем документ из байтов
    content = await file.read()
    doc = Document(BytesIO(content))

    # Применяем проверки
    orchestrator = CheckOrchestrator([
        StructureChecks(),
        PresenceChecks(),
        FontChecks()
    ])
    orchestrator.run(doc)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                              headers={"Content-Disposition": f"attachment; filename=checked_{file.filename}"})
