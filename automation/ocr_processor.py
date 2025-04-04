# Tesseract OpenCV
from PIL import Image
import pytesseract
from pytesseract import Output
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logs.logger import logger

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def transcreverCurriculo():
    try:
        print("##########################################")
        print("INICIANDO PROCESSO PARA TRANSCREVER IMAGEM")
        print("##########################################")

        imagem = Image.open("images/Curriculo.png")

        texto = pytesseract.image_to_string(imagem, lang="por")
        dados = pytesseract.image_to_data(imagem, lang="por", output_type=Output.DICT)
        boxes = pytesseract.image_to_boxes(imagem, lang="por")
        osd = pytesseract.image_to_osd(imagem)
        idiomas = pytesseract.get_languages()


        print(texto)
        # print(dados)
        # print(boxes)
        # print(osd)
        # print(idiomas)
        logger.info("ocr_processor executado com sucesso!")
    except Exception as e:
        logger.exception("Falha ao executar o ocr_processor!")

if __name__ == "__main__":
    transcreverCurriculo()

