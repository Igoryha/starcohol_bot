import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '5385998740:AAGTl4Jv7YeLmZhPcMuhX02vyHHpt7jyqIE'
TEXT: str = 'как тебе такое \U0001FAE5'
MAX_COUNTER: int = 10

offset: int = -2
counter: int = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1