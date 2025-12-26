from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

a = DefaultRouter()
a.register('',views.all)

urlpatterns = [
    path('',include(a.urls))
]