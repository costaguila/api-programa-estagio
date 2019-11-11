from django.contrib import admin
from django.urls import path
from apiEstagio.turismo.views import Turismo

urlpatterns = [
    path('', Turismo.as_view()),

]
