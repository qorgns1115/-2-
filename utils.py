# utils.py
from PIL import Image
import io

def generate_image(user_appearance: str, art_style: str):
    # 예시로 흰색 배경 이미지 생성
    img = Image.new('RGB', (100, 100), color = (255, 255, 255))
    return img

def image_to_blob(img: Image.Image):
    with io.BytesIO() as output:
        img.save(output, format="PNG")
        return output.getvalue()
