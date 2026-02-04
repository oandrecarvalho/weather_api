from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello_world, name='hello'),
    path('weather/<int:user_id>/today/', views.WeatherTodayView.as_view(), name='weather_today'),
    path('weather/<int:user_id>/next_day/', views.WeatherNextDayView.as_view(), name='weather_next_day'),
    path('weather/<int:user_id>/next_5_days/', views.WeatherNextFiveDaysView.as_view(), name='weather_next_5_days'),
]