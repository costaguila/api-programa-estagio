from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
class Turismo(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        url = staticfiles_storage.path('data.json')
        data = open(url).read()
        jsonData = json.loads(data)

        return Response(jsonData)
