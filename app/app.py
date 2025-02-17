from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsappCuadrado", methods=["POST"])
def whatsapp_reply():
    
    incoming_message= request.form.get("Body").strip()
    
    response= MessagingResponse()

    if incoming_message == "Hola":
        response.message("Hola mi nombre es cuadrado")
    else:
        response.message("Lo siento, este no es un mensaje valido")
        
    return str(response)

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


