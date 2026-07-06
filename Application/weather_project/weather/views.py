from django.shortcuts import render
from .forms import CityForm
from .services import get_weather_data


def home(request):
    weather_data = None
    form = CityForm()

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data["city"]

            data = get_weather_data(city)

            if data:
                weather_data = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "temp": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],
                    "pressure": data["main"]["pressure"],
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "description": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"],
                }

    context = {
        "form": form,
        "weather_data": weather_data
    }

    return render(request, "weather/home.html", context)