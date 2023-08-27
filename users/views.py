from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class UserCreateAPIView(CreateAPIView):
    pass


class UserListAPIView(ListAPIView):
    pass


class UserRetrieveAPIView(RetrieveAPIView):
    pass


class UserUpdateAPIView(UpdateAPIView):
    pass


class UserDestroyAPIView(DestroyAPIView):
    pass
