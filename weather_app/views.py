from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .services import WeatherService

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class WeatherTodayView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        location_query = f"{user.city},{user.state}".strip()
        weather_query = WeatherService.get_today_weather(location_query)

        if not weather_query :
            return Response({'detail': 'Meteorological data not found.'}, status.HTTP_400_BAD_REQUEST)


        formatted_weather_query = WeatherService.format_today_weather_response(user, weather_query)
        return Response({'today': formatted_weather_query}, status.HTTP_200_OK)


class WeatherNextDayView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        location_query = f"{user.city},{user.state}".strip()
        weather_query = WeatherService.get_weather_by_location(location_query)
        if not weather_query or not weather_query['list']:
            return Response({'detail': 'Meteorological data not found.'}, status.HTTP_400_BAD_REQUEST)

        formatted_weather_query = WeatherService.format_response(user, weather_query['list'][8])
        return Response({'next_day': formatted_weather_query}, status.HTTP_200_OK)


class WeatherNextFiveDaysView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        location_query = f"{user.city},{user.state}".strip()
        weather_query = WeatherService.get_weather_by_location(location_query)

        if not weather_query or not weather_query['list']:
            return Response({'detail': 'Meteorological data not found.'}, status.HTTP_404_NOT_FOUND)

        formatted_weather_query = [WeatherService.format_response(user, item) for item in weather_query['list'] if "15:00:00" in item['dt_txt']]
        return Response({'next_5_days': formatted_weather_query}, status.HTTP_200_OK)


def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello World'})

