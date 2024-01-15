import pyautogui
from time import sleep

# 1-Clicar e digitar usuário
pyautogui.click(694,386,duration=1)
pyautogui.write('Novis')
# 2-Clicar e digitar senha
pyautogui.click(693,409,duration=1)
pyautogui.write('novis2709')
# 3-Clicar e entrar
pyautogui.click(588,437,duration=1)
