from django.core.exceptions import ValidationError


def validate_time_complete(value):
    if value > 150:
        raise ValidationError('Время на выполнение не должно превышать 150 секунд')


def validate_related_habbit(value):
    if value and not value.useful:
        raise ValidationError('Привычка должна быть приятной')


def validate_period(value):
    if value < 7:
        raise ValidationError('Привычка выполняется 1 раз в 7 дней')
