from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

app.route("/whatsappCuadrado")
def whatsapp_reply():
    
    incoming_message= request.form.get("Body").strip()
    
    response= MessagingResponse()

    if incoming_message == "Hola":
        response.message("Hola mi nombre es cuadrado")
    else:
        response.message("Lo siento, este no es un mensaje valido")

if __name__ =="__main__":
    app.run(port='0.0.0.0', debug=True)


