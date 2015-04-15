from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models


UserModel = get_user_model()


class User(serializers.ModelSerializer):
    class Meta:
        model = UserModel

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        print('NEW '*20)


class MyUser(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=UserModel.objects.all())
    class Meta:
        model = models.MyUser


class User2(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        depth = 2

