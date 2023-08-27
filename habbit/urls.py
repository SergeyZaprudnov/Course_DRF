from django.urls import path

from habbit.apps import AppHabbitConfig
from habbit.views import HabbitListAPIView, HabbitCreateAPIView, HabbitRetrieveAPIView, HabbitUpdateAPIView, \
    HabbitDestroyAPIView

app_name = AppHabbitConfig.name

urlpatterns = [
    path('habbit/', HabbitListAPIView.as_view(), name='habbit_list'),
    path('habbit/create/', HabbitCreateAPIView.as_view(), name='habbit_create'),
    path('habbit/<int:pk>/', HabbitRetrieveAPIView.as_view(), name='habbit_get'),
    path('habbit/update/<int:pk>/', HabbitUpdateAPIView.as_view(), name='habbit_update'),
    path('habbit/delete/<int:pk>/', HabbitDestroyAPIView.as_view(), name='habbit_delete'),
]
