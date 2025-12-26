from django.shortcuts import render
from .models import user
from .serializers import seri
from rest_framework.viewsets import ModelViewSet

class all(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = seri
    

