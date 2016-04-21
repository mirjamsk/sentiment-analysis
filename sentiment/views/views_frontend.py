from django.shortcuts import render


def index(request):
    message = "Front-end under construction :)"
    context = {'message': message}
    return render(request, 'sentiment/index.html', context)
