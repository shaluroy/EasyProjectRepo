from django.urls import path
from testapp import views

urlpatterns=[
    path('hii/',views.hello),
]