from django.shortcuts import redirect,render
from . import models


def mainView(request):
    template_file = "proffesional/main.html"

    option = {

    }
    return render(request, template_file, option)

def result(request):
    template_file = "proffesional/result.html"

    option = {

    }
    return render(request, template_file, option)
