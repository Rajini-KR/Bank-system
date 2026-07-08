from .forms import CityForm
from .services import get_weather
from django.shortcuts import render
from .models import SearchHistory


def home(request):

    weather_data = None
    form = CityForm()
    error=None

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data["city"]
            weather_data = get_weather(city)
    else:
        error="Please enter a valid city name."
    history=SearchHistory.objects.all()[:5]


    context = {
        "form": form,
        "weather": weather_data,
        "error":error,
        "history":history
    }
    return render(request, 'weather/home.html',context)