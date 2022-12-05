import time

import pyautogui

bbpy = pyautogui
imgcontinue = pyautogui.locateOnScreen('imagens/continue.png', confidence=0.7)
imgignorar = pyautogui.locateOnScreen('imagens/ignorar.png', confidence=0.7)
imgignorar2 = pyautogui.locateOnScreen('imagens/ignorar2.png', confidence=0.7)
imgcheckbox = pyautogui.locateOnScreen('imagens/checkbox.png', confidence=0.7)
imgcheckbox2 = pyautogui.locateOnScreen('imagens/checkbox2.png', confidence=0.7)
def options():
    opcoes = bbpy.confirm('clique no botão desejado', buttons=['temp', '%temp%', 'Prefetch'])
    if opcoes == 'temp':
        CCCtemp()
    if opcoes == '%temp%':
        CCCtempP()
    if opcoes == 'Prefetch':
        CCCPrefetch()
def CCCtemp():
    bbpy.hotkey('win', 'r')
    bbpy.sleep(2)
    bbpy.typewrite('temp')
    bbpy.hotkey('enter')
    bbpy.sleep(3)
    bbpy.hotkey('ctrl', 'a')
    bbpy.sleep(2)
    bbpy.hotkey('shift', 'delete')
    bbpy.hotkey('enter')
    time.sleep(3)
    if imgcheckbox or imgcheckbox2:
       pass
    bbpy.sleep(2)
    if imgcontinue:
        pass
    if imgignorar:
        pass
    if imgignorar2:
        pass
    time.sleep(3)
    return options()


def CCCtempP():
    bbpy.hotkey('win','r')
    bbpy.sleep(2)
    bbpy.typewrite('%temp%')
    bbpy.hotkey('enter')
    bbpy.sleep(3)
    bbpy.hotkey('ctrl','a')
    bbpy.sleep(2)
    bbpy.hotkey('shift','delete')
    bbpy.hotkey('enter')
    time.sleep(2)
    print('clicou em delete')
    if imgcheckbox:
        pass
    if imgcontinue:
        pass
    bbpy.sleep(2)
    if imgignorar:
        pass
    if imgignorar2:
        pass
    time.sleep(3)
    return options()

    #LIMPANDO A PASTA prefetech
def CCCPrefetch():
    bbpy.hotkey('win','r')
    bbpy.sleep(2)
    bbpy.typewrite('prefetch')
    bbpy.hotkey('enter')
    bbpy.sleep(3)
    bbpy.hotkey('ctrl','a')
    bbpy.sleep(2)
    bbpy.hotkey('shift','delete')
    bbpy.hotkey('enter')
    time.sleep(2)
    if imgcheckbox:
        pass
    bbpy.sleep(2)
    if imgcontinue:
        pass
    if imgignorar:
        pass
    if imgignorar2:
        pass
    time.sleep(3)
    return options()


options()

