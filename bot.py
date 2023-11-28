from email.message import EmailMessage
import smtplib # Conexion con servidor de gmail

remitente = "areaanaliticaemergia@gmail.com"

destinatarios = ["lcastrov99@gmail.com",
                 "lcastrov@unal.edu.co",
                 "jharenasq@unal.edu.co",
                 "fyzapatac@unal.edu.co",
                 "aarualest@unal.edu.co",
                 "cristian.llanos40795@ucaldas.edu.co",
                 "natalia.betancurh@autonoma.edu.co",
                 "daniell9151@gmail.com",
                 "Jdgj9151@gmail.com",
                 "santycano4@gmail.com"]

mensaje = "Hola, el area mas visajosa de Emergia está realizando pruebas... Gracias 🤨"

for i in range(len(destinatarios)):
    email = EmailMessage()
    email['From'] = remitente
    email['To'] = destinatarios[i]
    email['Subject'] = "PRUEBA #3. El Area de Analítica de Emergia, te da la bienvenida 😊"
    email.set_content(mensaje)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "lenw xnqy apsw fbjf")
    smtp.sendmail(remitente, 
                    destinatarios[i],
                    email.as_string())

smtp.quit()
