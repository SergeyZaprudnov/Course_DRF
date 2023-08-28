from datetime import datetime

import requests
from celery import shared_task

from config import settings
from habbit.models import Habbit

telegram_api_token = settings.TELEGRAM_API_TOKEN
chat_id = settings.CHAT_ID


@shared_task
def telegram_message(habbit_id):
    habbit = Habbit.objects.get(id=habbit_id)
    habbit_time = habbit.time
    now = datetime.now().time()
    seconds_until_habbit = (datetime.combine(datetime.today(), habbit_time) - datetime.combine(datetime.today(),
                                                                                               now)).total_seconds()
    message = (
        f"Напоминание о привычке {habbit.user.telegram_username}:\n Место: {habbit.place}\n"
        f"Действие: {habbit.action}\n Время: {habbit.time}")
    url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "schedule_date": int(now.timestamp() + seconds_until_habbit)
    }
    response = requests.get(url, params=params)
