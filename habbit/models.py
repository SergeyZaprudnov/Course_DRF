from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habbit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=250, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=250, verbose_name='Действие')
    useful = models.BooleanField(default=False, verbose_name='Полезная привычка')
    related_habbit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')
    period = models.PositiveIntegerField(default=1, verbose_name='Периодичность в днях')
    reward = models.CharField(max_length=250, **NULLABLE, verbose_name='Награда')
    time_complete = models.PositiveIntegerField(verbose_name='Время выполнения')
    public = models.BooleanField(default=False, verbose_name='Публичность привычки')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
