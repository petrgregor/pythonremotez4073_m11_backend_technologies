from django.shortcuts import render

from viewer.models import Movie


def home(request):
    return render(request, 'home.html')


def movies(request):
    movies_ = Movie.objects.all()
    context = {'movies': movies_}
    return render(request=request,
                  template_name='movies.html',
                  context=context)

