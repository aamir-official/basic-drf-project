from rest_framework import serializers


class User(serializers.Serializer):
    id = serializers.IntegerField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
