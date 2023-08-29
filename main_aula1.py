import pandas as pd
import openpyxl 
import numpy
import tabula
import pyperclip as cl
from time import *
import pyautogui as gui


gui.press('win')
sleep(.8)
gui.write('chrome')
gui.press('enter')
sleep(.8)
cl.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
gui.hotkey('ctrl', 'v')
gui.press('enter')
sleep(5)
gui.doubleClick(347, 295)
sleep(3.5)
gui.click(452, 606, button='right')
sleep(3.5)
gui.click(478, 652)
sleep(4)
gui.press('enter')



tabela = pd.read_excel(r"C:\Users\W10\Downloads\Vendas - Dez.xlsx")
display(tabela)
