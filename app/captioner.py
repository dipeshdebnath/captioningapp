from transformers import VisionEncoderDecoderModel, AutoTokenizer, AutoImageProcessor
from PIL import Image
import torch

# Load model components
MODEL_NAME = "cnmoro/tiny-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
image_processor = AutoImageProcessor.from_pretrained(MODEL_NAME)

# Ensure model runs on CPU for lightweight deployment
device = torch.device("cpu")
model.to(device)

def generate_caption(image: Image.Image) -> str:
    # Preprocess image
    pixel_values = image_processor(images=image, return_tensors="pt").pixel_values.to(device)

    # Generate caption
    generated_ids = model.generate(pixel_values, max_length=64, num_beams=3)
    caption = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    return caption
