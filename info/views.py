from django.shortcuts import render
from rest_framework import viewsets
from info.models import User
from info.serializers import userSerializers

class InfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers

