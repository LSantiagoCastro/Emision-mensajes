import requests

from telegram import User
# from telegram.ext import Updater

TOKEN = "6872973688:AAG6ai4t1beLYwsBEoeS9lYyDIAo3FA1C8s"
text="Hola Mundo"


def get_chat_id_from_phone_number(phone_number):
    updater = Updater(token=TOKEN, use_context=True)
    user = User(id=0, first_name='', last_name='', username='', language_code='')
    chat = updater.bot.get_chat(phone_number, user)
    return chat.id


# def send_messages(phone_number, text):
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
#     params = {"chat_id": phone_number, "text": text}
#     response = requests.post(url, params=params)
#     return response
def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response


id = get_chat_id_from_phone_number("+573204259649")
print(f"ID extraido: {id}")
response = send_messages(id, text)
print(f"Response: {response}")
