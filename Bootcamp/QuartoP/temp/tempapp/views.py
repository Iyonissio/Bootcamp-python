from django.shortcuts import render


def index(request):
    return render(request, 'basic_app/index.html/')

def relative(request):
    return render(request, 'basic_app/relative.html/')

def other(request):
    return render(request, 'basic_app/other.html/')


