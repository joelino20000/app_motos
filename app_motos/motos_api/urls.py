#motos_api/urls.py

from django.urls import path
from .views import MotoListApiView, MotoDetailApiView

urlpatterns = [
    path('',MotoListApiView.as_view(), name="Moto_list"),
    path('<int:moto_id>/', MotoDetailApiView.as_view(), name="Moto_detail"),
]
