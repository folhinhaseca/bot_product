#AUTOMAÇÃO DE BOOT PARA CADASTRO DE PRODUTOS
import datetime
import pyautogui
import time
import pandas
pyautogui.PAUSE =0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.click(x=715, y=77)
pyautogui.click(x=675, y=374)
pyautogui.write("dessa.xpp@hotmail.com")
pyautogui.press("tab")
pyautogui.write("legalprogramar")
pyautogui.press("tab") 
pyautogui.press("enter")
time.sleep (1) 
tabela = pandas.read_csv("produtos.csv")
print(tabela)
pyautogui.click(x=663, y=255)
for linha in tabela.index:
    pyautogui.click (x=663, y=255)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write ((codigo))
    pyautogui.press ("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write ((marca))
    pyautogui.press ("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write ((tipo))
    pyautogui.press ("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write (str(categoria))
    pyautogui.press ("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write (str(preco_unitario))
    pyautogui.press ("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write (str(custo))
    pyautogui.press ("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write (str(obs))
    pyautogui.press ("tab")
    pyautogui.press ("enter")
    pyautogui.scroll (10000)

        