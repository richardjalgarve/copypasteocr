# ocr.py
from PIL import Image
import pytesseract

class OCR:
    def __init__(self, lang='eng'):
        self.lang = lang
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


    def extract_text(self, image_path):
        try:
            # Carrega a imagem
            image = Image.open(image_path)
            # Extrai o texto da imagem
            text = pytesseract.image_to_string(image, lang=self.lang)
            return text
        except Exception as e:
            return f"Erro ao processar a imagem: {e}"
