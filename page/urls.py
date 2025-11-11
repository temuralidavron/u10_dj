from django.urls import path
from .views import list_phone, create_phone

urlpatterns = [
    path("", list_phone, name="list"),
    path('create/',create_phone,name='create'),
]
