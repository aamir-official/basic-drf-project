from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers


SAMPLE_DATA = [{
    'id': 1,
    'firstname': 'john',
    'lastname': 'doe',
}, {
    'id': 2,
    'firstname': 'sarah',
    'lastname': 'connor',
}]


class User(viewsets.ViewSet):
    def list(self, request):
        queryset = SAMPLE_DATA
        serializer = serializers.User(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = dict((str(item['id']), item) for item in SAMPLE_DATA)
        print(queryset)
        user = queryset.get(pk, None)
        if not user:
            raise Http404("User does not exist")
        serializer = serializers.User(user)
        return Response(serializer.data)
