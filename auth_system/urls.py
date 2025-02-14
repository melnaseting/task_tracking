from django.urls import path
from auth_system import views

urlpatterns = [
    path('',views.base, name='base'),
    path("register/",views.register, name="register"),
    path("log-in/",views.log_in, name="log-in"),
    path("log-out/",views.CustomLogoutView.as_view(), name="log_out")
]