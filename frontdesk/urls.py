from django.urls import path
from . import views

app_name="frontdesk"

urlpatterns= [
    path('', views.home, name="home"),
    path('signup/', views.sign_up, name="sign_up"),
    path('login/', views.login, name="login"),
    path('thanks/', views.success_message, name="thanks")
]
