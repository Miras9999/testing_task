from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def testing_link(request):
    return render(request, 'core/testing_link.html')
