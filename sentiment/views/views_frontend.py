from django.shortcuts import render
from ..models import SentimentApiStats

def index(request):
    message = "Front-end under construction :)"
    context = {'message': message}
    return render(request, 'sentiment/index.html', context)


def stats(request):
    stats = SentimentApiStats.objects.all()
    context = {'stats': stats}
    return render(request, 'sentiment/stats.html', context)