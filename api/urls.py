
from django.urls import path
from api import views

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('works/',views.getWorks,name='get-works'),
]