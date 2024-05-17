import os 
from email.message import EmailMessage
import ssl
import smtplib

passwd = "ejem plod cont abcd" #contraseña de aplicacion aquí,  16 digitos en total 

email_sender = "tu_email@gmail.com"  #email desde donde se envia el mensaje 


email_receivers = ["ejemplo@gmail.com","ejemplo_email@gmail.com"] # puedes poner tantos como quieras receptores como quieras, se enviaran de uno en uno 



subject = "Asunto del email aqui "
body = " el cuerpo del mensaje que quieres enviar aqui"

# Ruta del archivo que deseas adjuntar
archivo_adjunto ="C:/Users/Usuario/Documents/python_Docs/interest_calculator.py" 
# Reemplaza 'ruta_del_archivo' con la ruta real de tu archivo

for i in email_receivers:
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = i
    em["Subject"] = subject
    em.set_content(body)

    # Adjuntar el archivo
    with open(archivo_adjunto, "rb") as archivo:
        contenido_adjunto = archivo.read()
        nombre_archivo = os.path.basename(archivo_adjunto)
    em.add_attachment(contenido_adjunto, maintype="application", subtype="octet-stream", filename=nombre_archivo)

    context = ssl.create_default_context()


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, passwd)
            smtp.sendmail(email_sender, i, em.as_string())
        print("Correo enviado con éxito.")
    except Exception as e:
        print("Error al enviar el correo:", e)

