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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        raise NotImplementedError()
        from rest_framework.response import Response
        return Response(serializer.data, status=201, headers=headers)



class UserList(generics.ListCreateAPIView):
    serializer_class = serializers.User2
    queryset = UserModel.objects.all()

