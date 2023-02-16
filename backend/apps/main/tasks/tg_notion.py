from django.conf import settings
import requests


def tg_msg(order: dict):
    # {settings.CITY[int(order["city"])][1]}
    msg = f'{order["summary"]} ₸ \n {order["fio"]} - {order["phone"]} \n | {order["street"]} | {order["house"]}'
    url_req = settings.BOT_URL + "/sendMessage" + "?chat_id=" + settings.BOT_CHAT_ID + "&text=" + msg
    requests.get(url_req)


