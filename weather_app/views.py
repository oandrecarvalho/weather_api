from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .services import WeatherService
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]



class WeatherTodayView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        location_query = f"{user.city},{user.state}".strip()
        weather_query = WeatherService.get_today_weather(location_query)

        if not weather_query :
            return Response({'detail': 'Meteorological data not found.'}, status.HTTP_404_NOT_FOUND)


        formatted_weather_query = WeatherService.format_today_weather_response(user, weather_query)
        return Response({'today': formatted_weather_query}, status.HTTP_200_OK)


class WeatherNextDayView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        location_query = f"{user.city},{user.state}".strip()
        weather_query = WeatherService.get_weather_by_location(location_query)
        if not weather_query or not weather_query['list']:
            return Response({'detail': 'Meteorological data not found.'}, status.HTTP_404_NOT_FOUND)

        formatted_weather_query = WeatherService.format_response(user, next((item for item in weather_query['list'] if "15:00:00" in item.get('dt_txt', '')), weather_query['list'][8]))
        return Response({'next_day': formatted_weather_query}, status.HTTP_200_OK)


class WeatherNextFiveDaysView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        location_query = f"{user.city},{user.state}".strip()
        weather_query = WeatherService.get_weather_by_location(location_query)

        if not weather_query or not weather_query['list']:
            return Response({'detail': 'Meteorological data not found.'}, status.HTTP_404_NOT_FOUND)

        formatted_weather_query = [WeatherService.format_response(user, item) for item in weather_query['list'] if "15:00:00" in item['dt_txt']]
        return Response({'next_5_days': formatted_weather_query}, status.HTTP_200_OK)

@login_required(login_url='/login/')
def index(request):
    context = {}
    if request.method == 'POST':
        action = request.POST.get('action')
        user = request.user
        location_query = f"{user.city},{user.state}"

        if action == 'today':
            weather_query = WeatherService.get_today_weather(location_query)
            context['today'] = WeatherService.format_today_weather_response(user, weather_query)

        elif action == 'next_day':
            weather_query = WeatherService.get_weather_by_location(location_query)
            tomorrow_forecast = next((item for item in weather_query['list'][8:] if "15:00:00" in item['dt_txt']), weather_query['list'][8])
            context['next_day'] = WeatherService.format_response(user, tomorrow_forecast)

        elif action == 'next_5_days':
            data = WeatherService.get_weather_by_location(location_query)
            context['next_5_days'] = [WeatherService.format_response(user, item)for item in data['list'] if "15:00:00" in item['dt_txt']]

    return render(request, 'weather_page/index.html', context)


def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        if 'email' in data:
            data['username'] = data['email']

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')

    return render(request, 'users_page/register.html')


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello World'})

