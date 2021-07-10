from django.urls import path
from accounts.views import base

app_name = 'accounts'

urlpatterns = [
    path('', base, name='base')
]