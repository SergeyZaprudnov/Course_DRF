from datetime import datetime

import requests
from celery import shared_task

from config import settings
from habbit.models import Habbit
from users.models import User

telegram_api_token = settings.TELEGRAM_API_TOKEN
chat_id = settings.CHAT_ID


@shared_task
def update_telegram_ids():
    method = '/getUpdates'
    url = settings.TELEGRAM_URL + settings.TELEGRAM_API_KEY + method
    response = requests.get(url)
    updates = response.json()['result']
    for update in updates:
        if update['message']['entities'][0]['type'] == 'email':
            email = update['message']['text']
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                user.telegram_id = update['message']['chat']['id']
                user.save()
    if updates:
        requests.get(
            url,
            params={'offset': updates[-1]['update_id'] + 1}
        )


@shared_task
def send_notifications():
    method = '/sendMessage'
    url = settings.TELEGRAM_URL + settings.TELEGRAM_API_KEY + method
    for user in User.objects.all():
        if not user.telegram_id:
            continue
        message = (f"Привет!"
                   f"Вот Ваши привычки на сегодня!\n")
        habits = Habbit.objects.filter(owner=user).order_by('time')
        for habit in habits:
            diff = datetime.date.today() - habit.created_on
            if diff.days % habit.period != 0:
                continue
            elif not habit.is_pleasant:
                message += (
                    f"*{habit.time.strftime('%H:%M')}*"
                    f" - {habit.action.upper()} in {habit.place}\n\n"
                )
        params = {
            'chat_id': user.telegram_id,
            'text': message,
            'parse_mode': 'MarkdownV2'
        }
        requests.post(
            url,
            params=params,
        )
