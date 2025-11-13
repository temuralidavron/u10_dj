from django.urls import path
from .views import list_phone, create_phone, detail_phone, phone_update

urlpatterns = [
    path("", list_phone, name="list"),
    path('create/',create_phone,name='create'),
    path("detail/<int:pk>/",detail_phone,name='detail'),
    path("update/<int:pk>/",phone_update,name='update'),
]
