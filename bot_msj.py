from twilio.rest import Client
import keys

client  = Client(keys.account_sid, keys.auth_token)
message = client.messaes.create(
    body = "Prueba mensajes de texto. Area Analitica Emergia",
    from_= keys.twilio_number,
    to=keys.my_phone_number
)

print(message.body)

