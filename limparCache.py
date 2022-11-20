import cv2
import pyautogui

bbpy = pyautogui
opcoes = bbpy.confirm('clique no botão desejado', buttons=['temp','%temp%','Prefetch'])

if opcoes == 'temp':
    # LIMPANDO A PASTA TEMP
    bbpy.hotkey('win','r')
    bbpy.sleep(2)
    bbpy.typewrite('temp')
    bbpy.hotkey('enter')
    bbpy.sleep(3)
    bbpy.hotkey('ctrl','a')
    bbpy.sleep(2)
    bbpy.hotkey('shift','delete')
    posicaoTela = pyautogui.locateOnScreen('imagens/checkbox.png', confidence=0.9)
    bbpy.click(posicaoTela)
    bbpy.sleep(5)
    bbpy.hotkey('enter')

if opcoes == '%temp%':
    #LIMPANDO A PASTA %TEMP%
    bbpy.hotkey('win','r')
    bbpy.sleep(2)
    bbpy.typewrite('%temp%')
    bbpy.hotkey('enter')
    bbpy.sleep(3)
    bbpy.hotkey('ctrl','a')
    bbpy.sleep(2)
    bbpy.hotkey('shift','delete')
    posicaoTela = pyautogui.locateOnScreen('imagens/ignorar.png', confidence=0.8)
    bbpy.sleep(4)
    bbpy.click(posicaoTela)
    bbpy.sleep(5)


if opcoes == 'Prefetch':
    #LIMPANDO A PASTA prefetech
    bbpy.hotkey('win','r')
    bbpy.sleep(2)
    bbpy.typewrite('prefetch')
    bbpy.hotkey('enter')
    bbpy.sleep(3)
    bbpy.hotkey('ctrl','a')
    bbpy.sleep(2)
    bbpy.hotkey('shift','delete')
    bbpy.sleep(5)
    bbpy.hotkey('enter')