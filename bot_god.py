import pandas as pd
import webbrowser as web
import pyautogui as pg
import time
from email.message import EmailMessage
import smtplib # Conexion con servidor de gmail

data = pd.read_excel("Clientes.xlsx", sheet_name='Ventas')
# data.head(3)
print("Archivo cargado con exito\n")

# ENVIO DE CORREOS
data_correo = data.query("Correo.notna()").reset_index(drop=True)
print("Registros con correo")
print(data_correo)
print('')

remitente = "areaanaliticaemergia@gmail.com"
destinatarios = data_correo['Correo']
nombres = data_correo['Nombre']
for i in range(len(destinatarios)):
    try:
        mensaje = f"Hola {nombres[i]} 👋, en nombre de todo el equipo de Analítica de emergia, te extendemos un cálido saludo y agradecemos tu presencia. "+"""Estás a punto de vivir una experiencia inolvidable.\n\n\n ¡Disfruta al máximo! 😁 ¡Tu viaje hacia la analítica y la inteligencia artificial comienza ahora! 🌟"""
        
        email = EmailMessage()
        email['From'] = remitente
        email['To'] = destinatarios[i]
        email['Subject'] = "El Área de Analítica y Estrategia de Negocio de emergia, te da la bienvenida 😊"
        email.set_content(mensaje)

        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitente, "lenw xnqy apsw fbjf")
        smtp.sendmail(remitente, 
                        destinatarios[i],
                        email.as_string())
        print(f"Correo electrónico de {nombres[i]} enviado con éxito")
    except:
        print(f"Email {destinatarios[i]} de {nombres[i]} erroneo. Correo no enviado\n")
smtp.quit()
print("Envío de correos Finalizado\n")

# # ENVIO DE MENSAJES DE WHATSAPP
# data_W = data.query("Celular.notna()").reset_index(drop=True)
# print("Registros con celular")
# print(data_W)
# print('')

# for i in range(len(data_W)):
#     try:
#         celular = data_W.loc[i,'Celular'].astype(str) # Convertir a string para que se añada al mensaje
#         nombre = data_W.loc[i,'Nombre']
#         # producto = data_W.loc[i,'Producto']
        
#         # Crear mensaje personalizado
#         mensaje = f"Hola {nombre} 👋, en nombre de todo el equipo de Analítica y Estrategia de Negocio de emergia 🖥️, te extendemos un cálido saludo y agradecemos tu presencia. "+"""Estás a punto de vivir una experiencia inolvidable 🧠.\n\n\n ¡Disfruta al máximo! 😁 ¡Tu viaje hacia la analítica y la inteligencia artificial comienza ahora! 🌟"""
                    
#         # Abrir una nueva pestaña para entrar a WhatsApp Web
#         # Opción 1: Si te abre WhastApp Web directamente en Google Chrome
#         web.open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)
        
#         # Opción 2: Si te abre WhastApp Web en Microsoft Edge, especificar que lo abra en Chrome
#         # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#         # web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)
        
#         time.sleep(8)           # Esperar 8 segundos a que cargue
#         pg.click(1230,964)      # Hacer click en la caja de texto
#         time.sleep(2)           # Esperar 2 segundos 
#         pg.press('enter') 
#         pg.click(1838, 945)# Enviar mensaje 
#         time.sleep(3)           # Esperar 3 segundos a que se envíe el mensaje
#         pg.hotkey('ctrl', 'w')  # Cerrar la pestaña
#         time.sleep(2)
#         print(f"Msj Whatsapp de {nombre} enviado con éxito")
#     except:
#         print(f"Email {celular} de {nombre} erroneo. Mensaje de whatsapp no enviado\n")

# print("Mensajes de whatsapp enviados")


