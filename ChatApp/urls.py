from django.urls import path,include
from ChatApp import views as ChatApp_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path ("", ChatApp_views.ChatPage, name="ChatApp-page"),
    path("auth/Login", LoginView.as_view
            (template_name="ChatApp/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
