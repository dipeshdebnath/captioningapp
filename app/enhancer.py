from transformers import pipeline

uplift = pipeline("text2text-generation", model="mrm8488/t5-base-finetuned-positive-sentiment")

def enhance_caption(caption: str) -> str:
    return uplift(caption)[0]["generated_text"]
