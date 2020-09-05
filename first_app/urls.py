from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('logup/',views.logup,name='logup'),
    path('singout/',views.singout,name='singout'),
    path('search/<user>-<password>/',views.search,name='search'),
    path('home/<user>-<password>/',views.home,name='home'),
    path('songSerch/<user>-<password>/',views.songSerch,name='songSerch'),
    path('analysis/<user>-<password>',views.analysis,name='analysis'),

]
