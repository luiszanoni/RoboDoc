# PyAutoGUI
import pyautogui
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logs.logger import logger

class DesktopAutomation:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
        self.IMAGE_PATH = os.path.join(self.BASE_DIR, "images")
        self.IMAGE_PATHS = [os.path.join(self.IMAGE_PATH, "textsize.png"), os.path.join(self.IMAGE_PATH, "textsize36.png")]
        self.localizacaosize = None
        self.largura, self.altura = pyautogui.size()

        self.x, self.y = 300, 400
        self.espaco_entre_letras = 80 

    def automatizacaopaint(self):
        print("###################################################################")
        print("INICIANDO PROCESSO AUTOMATIZADO DE NAVEGACAO DE SISTEMA OPERACIONAL")
        print("###################################################################")
        try:
            pyautogui.PAUSE = 1
            pyautogui.FAILSAFE = True
            
            pyautogui.hotkey("win", "r")
            pyautogui.write("mspaint")
            pyautogui.press("enter")
            1
            localizacaotext = pyautogui.locateOnScreen(os.path.join(self.IMAGE_PATH, "texticon.png"), confidence=0.8)
            pyautogui.click(localizacaotext)
            
            localizacaobold = pyautogui.locateOnScreen(os.path.join(self.IMAGE_PATH, "textbold.png"), confidence=0.8)

            center_x, center_y = pyautogui.center(localizacaobold)
            adjusted_x = center_x - 100
            
            pyautogui.click(adjusted_x, center_y)

            pyautogui.typewrite('36')
            
            pyautogui.click(self.x,self.y)
            pyautogui.dragTo(self.x+1000, self.y+400)
            
            pyautogui.typewrite('Automatizacao feita por Luis Gustavo Zanoni')
            pyautogui.press('enter')
            pyautogui.typewrite('Linkedin: https://www.linkedin.com/in/luiszanoni/')
            pyautogui.press('enter')
            pyautogui.typewrite('Github: https://github.com/luiszanoni')

            logger.info("desktop_automation executado com sucesso!")
        except Exception as e:
            logger.exception("Falha ao executar o desktop_automation")

if __name__ == "__main__":
    automacao = DesktopAutomation()
    automacao.automatizacaopaint()