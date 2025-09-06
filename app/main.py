from fastapi import FastAPI, UploadFile, File
from app.captioner import generate_caption
from app.enhancer import enhance_caption
from app.utils import load_image

app = FastAPI()

@app.post("/caption")
async def caption_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = load_image(image_bytes)
    raw_caption = generate_caption(image)
    enhanced = enhance_caption(raw_caption)
    return {
        "raw_caption": raw_caption,
        "enhanced_caption": enhanced
    }
