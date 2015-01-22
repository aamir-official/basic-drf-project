# from django.views.decorators.cache import cache_page
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
# from rest_framework.response import Response
from . import serializers, models


UserModel = get_user_model()


class User(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = serializers.User

    def list(self, request, **kwargs):
        return super(User, self).list(request, **kwargs)

    def retrieve(self, request, **kwargs):
        return super(User, self).retrieve(request, **kwargs)


class MyUser(ModelViewSet):
    queryset = models.MyUser.objects.all()
    serializer_class = serializers.MyUser

    def list(self, request, **kwargs):
        print('*' * 80)
        print(self.queryset.all())
        return super(MyUser, self).list(request, **kwargs)


class UserList(generics.ListCreateAPIView):
    serializer_class = serializers.User2
    queryset = UserModel.objects.all()

