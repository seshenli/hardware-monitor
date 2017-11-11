from django.shortcuts import render


def index(request):
    return render(request, "index.html")
# def index(request):
#     return render(request, "table.html")


def user(request):
    return render(request, "user.html")


def table(request):
    return render(request, "table.html")
