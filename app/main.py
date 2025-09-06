from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from app.captioner import generate_caption

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "I am Captionapp"}

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    # Load image from upload
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Generate caption
    caption = generate_caption(image)
    return {"caption": caption}
