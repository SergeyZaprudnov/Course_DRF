from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habbit.models import Habbit
from habbit.pagination import MyPagination
from habbit.permissions import IsPublicOrReadOnly, IsOwnerOrReadOnly
from habbit.serialisers import HabbitSerializer


class HabbitCreateAPIView(CreateAPIView):
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class HabbitListAPIView(ListAPIView):
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsPublicOrReadOnly]
    pagination_class = MyPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habbit.objects.filter(Q(public=True) | Q(user=user))
        else:
            return Habbit.objects.filter(public=True)


class HabbitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Habbit.objects.all()


class HabbitUpdateAPIView(UpdateAPIView):
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Habbit.objects.all()


class HabbitDestroyAPIView(DestroyAPIView):
    queryset = Habbit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
