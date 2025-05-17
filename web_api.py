from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from io import BytesIO
from docx import Document

from runner import run_checks_doc  # импорт универсальной функции

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI is running!"}

@app.post("/check_doc/")
async def check_doc(file: UploadFile = File(...)):
    file_bytes = await file.read()
    doc = Document(BytesIO(file_bytes))

    checked_doc = run_checks_doc(doc)

    out_stream = BytesIO()
    checked_doc.save(out_stream)
    out_stream.seek(0)

    return StreamingResponse(
        out_stream,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f"attachment; filename=checked_{file.filename}"}
    )