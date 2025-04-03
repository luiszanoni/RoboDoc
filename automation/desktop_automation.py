# PyAutoGUI Pywinauto
import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.FAILSAFE = True

largura, altura = pyautogui.size()
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

x, y = 300, 400
espaco_entre_letras = 80 


def desenhar_natalia_te_amo():
    global x, y
    
    # "N"
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x, y + 100, duration=0.5)
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)
    pyautogui.moveTo(x + 50, y)
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)
    x += espaco_entre_letras  


    # "A"
    pyautogui.moveTo(x, y + 100)
    pyautogui.dragTo(x + 25, y, duration=0.5)
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)
    pyautogui.moveTo(x + 15, y + 50)
    pyautogui.dragTo(x + 35, y + 50, duration=0.3)
    x += espaco_entre_letras  


    # "T"
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x + 50, y, duration=0.5)
    pyautogui.moveTo(x + 25, y)
    pyautogui.dragTo(x + 25, y + 100, duration=0.5)
    x += espaco_entre_letras  


    # "A"
    pyautogui.moveTo(x, y + 100)
    pyautogui.dragTo(x + 25, y, duration=0.5)  
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)  
    pyautogui.moveTo(x + 15, y + 50)
    pyautogui.dragTo(x + 35, y + 50, duration=0.3)  
    x += espaco_entre_letras  


    # "L"
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x, y + 100, duration=0.5)  
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)  
    x += espaco_entre_letras  


    # "I"
    pyautogui.moveTo(x + 25, y)
    pyautogui.dragTo(x + 25, y + 100, duration=0.5)  
    x += espaco_entre_letras  


    # "A"
    pyautogui.moveTo(x, y + 100)
    pyautogui.dragTo(x + 25, y, duration=0.5)  
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)  
    pyautogui.moveTo(x + 15, y + 50)
    pyautogui.dragTo(x + 35, y + 50, duration=0.3)  
    x += espaco_entre_letras + 20  


    # "T"
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x + 50, y, duration=0.5)  
    pyautogui.moveTo(x + 25, y)
    pyautogui.dragTo(x + 25, y + 100, duration=0.5)  
    x += espaco_entre_letras  


    # "E"
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x, y + 100, duration=0.5)  
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)  
    pyautogui.moveTo(x, y + 50)
    pyautogui.dragTo(x + 40, y + 50, duration=0.3)  
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x + 50, y, duration=0.5)  
    x += espaco_entre_letras + 20  


    # "A"
    pyautogui.moveTo(x, y + 100)
    pyautogui.dragTo(x + 25, y, duration=0.5)  
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)  
    pyautogui.moveTo(x + 15, y + 50)
    pyautogui.dragTo(x + 35, y + 50, duration=0.3)  
    x += espaco_entre_letras  


    # "M"
    pyautogui.moveTo(x, y + 100)
    pyautogui.dragTo(x, y, duration=0.5)  
    pyautogui.dragTo(x + 25, y + 50, duration=0.5)  
    pyautogui.dragTo(x + 50, y, duration=0.5)  
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)  
    x += espaco_entre_letras  


    # "O"
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x, y + 100, duration=0.5)  
    pyautogui.dragTo(x + 50, y + 100, duration=0.5)  
    pyautogui.dragTo(x + 50, y, duration=0.5)  
    pyautogui.dragTo(x, y, duration=0.5)  

def automatizacaopaint():
    localizacaotext = pyautogui.locateOnScreen('texticon.png')
    pyautogui.click(localizacaotext)
    localizacaosize = pyautogui.locateOnScreen('textsize.png')
    pyautogui.click(localizacaosize)
    pyautogui.typewrite('36')
    
    pyautogui.click(x,y)
    pyautogui.dragTo(x+1000, y+400)
    
    pyautogui.typewrite('Automatizacao feita por Luis Gustavo Zanoni')
    pyautogui.press('enter')
    pyautogui.typewrite('Linkedin: https://www.linkedin.com/in/luiszanoni/')
    pyautogui.press('enter')
    pyautogui.typewrite('Github: https://github.com/luiszanoni')

automatizacaopaint()