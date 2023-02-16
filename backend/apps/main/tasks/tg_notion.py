# from django.conf import settings
import requests

BOT_TOKEN = '5554883324:AAFltxc8VPuXdVYqhr_k13kU7aAU9uzkJNo'
BOT_URL = "https://api.telegram.org/bot" + BOT_TOKEN
BOT_CHAT_ID = '832855518'


def tg_msg(text):
    url_req = BOT_URL + "/sendMessage" + "?chat_id=" + BOT_CHAT_ID + "&text=" + text
    res = requests.get(url_req)


if __name__ == '__main__':
    tg_msg('Mura')
