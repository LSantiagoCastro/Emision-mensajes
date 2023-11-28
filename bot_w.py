import pandas as pd
import webbrowser as web
import pyautogui as pg
import time

data = pd.read_excel("Clientes.xlsx", sheet_name='Ventas')
# data.head(3)
print("Archivo cargado con exito\n")
# data = data.loc[[9],:]
for i in range(len(data)):
    celular = data.loc[i,'Celular'].astype(str) # Convertir a string para que se añada al mensaje
    nombre = data.loc[i,'Nombre']
    # producto = data.loc[i,'Producto']
    
    # Crear mensaje personalizado
    mensaje = f"Hola {nombre} 👋, en nombre de todo el equipo de Analítica de Emergia, te extendemos un cálido saludo y agradecemos tu presencia. "+"""Estás a punto de vivir una experiencia inolvidable en el mundo de la analítica de datos y la inteligencia artificial 🧠.\n\n\n ¡Disfruta al máximo! 😁 ¡Tu viaje hacia la analítica y la inteligencia artificial comienza ahora! 🌟"""
                
    # Abrir una nueva pestaña para entrar a WhatsApp Web
    # Opción 1: Si te abre WhastApp Web directamente en Google Chrome
    web.open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)
    
    # Opción 2: Si te abre WhastApp Web en Microsoft Edge, especificar que lo abra en Chrome
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)
    
    time.sleep(8)           # Esperar 8 segundos a que cargue
    pg.click(1230,964)      # Hacer click en la caja de texto
    time.sleep(2)           # Esperar 2 segundos 
    pg.press('enter') 
    pg.click(1838, 945)# Enviar mensaje 
    time.sleep(3)           # Esperar 3 segundos a que se envíe el mensaje
    pg.hotkey('ctrl', 'w')  # Cerrar la pestaña
    time.sleep(2)
    