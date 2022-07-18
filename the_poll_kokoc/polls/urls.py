from django.urls import path, include

from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('take_poll/<int:poll_id>/', views.take_poll, name='take_poll'),
    path('shop/', views.shop, name='shop'),
    path('profile/', views.profile, name='profile'),
    path('leaderboard/', views.leaderboard, name='leaderboard')
]
