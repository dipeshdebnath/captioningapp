import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Dipesh's Creator API 🚀"}

@app.post("/caption")
async def generate_caption(file: UploadFile = File(...)):
    # Placeholder logic — replace with actual model inference
    filename = file.filename
    content = await file.read()
    size_kb = round(len(content) / 1024, 2)

    # Simulated caption
    caption = f"This image ({filename}, {size_kb} KB) looks stunning. ✨"

    return JSONResponse(content={"caption": caption})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port)
