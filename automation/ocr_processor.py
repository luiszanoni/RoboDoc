# Tesseract OpenCV
from PIL import Image
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

imagem = Image.open("Curriculo.png")

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

