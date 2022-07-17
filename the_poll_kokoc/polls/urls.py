from django.urls import path, include

from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('take_poll/<int:poll_id>/', views.take_poll, name='take_poll')
]
