from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello, World")


def hello2(request, s):
    return HttpResponse(f"Hello, {s} world!")


def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f"Hello, {s} world!")


def hello4(request, s):
    t = request.GET.get('t', '')
    return HttpResponse(f"Your words: {s}, {t}")


def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")


def add2(request):
    # http://127.0.0.1:8000/add2 -> 0 + 0 = 0
    # http://127.0.0.1:8000/add2?num1=5 -> 5 + 0 = 5
    # http://127.0.0.1:8000/add2?num2=9 -> 0 + 9 = 9
    # http://127.0.0.1:8000/add2?num1=5&num2=7 -> 5 + 7 = 12
    # http://127.0.0.1:8000/add2?num2=5&num1=7 -> 7 + 5 = 12
    # http://127.0.0.1:8000/add2?num2=5&num1=7&num3=8 -> 7 + 5 = 12
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")
