from django.contrib import admin
from django.conf.urls import url
from apiEstagio.turismo.views import Turismo

urlpatterns = [
    url(r'^$', Turismo.as_view(),name='turismo'),

]
