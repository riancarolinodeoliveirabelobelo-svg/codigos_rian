#estou importndo o pyautogui e aprlidando ele de aut
import pyautogui as aut

#pressiono a tecla de atalho win +r
aut.hotkey('win','r')
#escreva notepad
aut.write('notepad', interval=0.7)
#espera 1 segundo
aut.sleep(1)
#aperta o EnvironmentError
aut.press('enter')
