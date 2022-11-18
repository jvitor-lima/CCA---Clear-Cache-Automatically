import cv2
import pyautogui

abrirarq = pyautogui
#LIMPANDO A PASTA TEMP
# abrirarq.hotkey('win','r')
# abrirarq.sleep(2)
# abrirarq.typewrite('temp')
# abrirarq.hotkey('enter')
# abrirarq.sleep(3)
# abrirarq.hotkey('ctrl','a')
# abrirarq.sleep(2)
# abrirarq.hotkey('shift','delete')
# posicaoTela = pyautogui.locateOnScreen('imagens/checkbox.png', confidence=0.9)
# abrirarq.click(posicaoTela)
# abrirarq.sleep(5)
# abrirarq.hotkey('enter')
#



# #LIMPANDO A PASTA %TEMP%
abrirarq.hotkey('win','r')
abrirarq.sleep(2)
abrirarq.typewrite('%temp%')
abrirarq.hotkey('enter')
abrirarq.sleep(3)
abrirarq.hotkey('ctrl','a')
abrirarq.sleep(2)
abrirarq.hotkey('shift','delete')
posicaoTela = pyautogui.locateOnScreen('imagens/ignorar.png', confidence=0.8)
abrirarq.sleep(4)
abrirarq.click(posicaoTela)
abrirarq.sleep(5)

# #LIMPANDO A PASTA prefetech
# abrirarq.hotkey('win','r')
# abrirarq.sleep(2)
# abrirarq.typewrite('prefetch')
# abrirarq.hotkey('enter')
# abrirarq.sleep(3)
# abrirarq.hotkey('ctrl','a')
# abrirarq.sleep(2)
# abrirarq.hotkey('shift','delete')
# abrirarq.sleep(5)
# abrirarq.hotkey('enter')