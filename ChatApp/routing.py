from django.urls import path, include
from .consumers import ChatAppConsumers


websocket_urlpatterns =[
    path("",ChatAppConsumers.as_asgi()),
]