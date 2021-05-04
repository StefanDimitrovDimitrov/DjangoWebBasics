from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView

from django101.models import Game


def index(request):
    title = 'SoftUni Django 101'
    user = User.objects.all()
    context = {
        'title': title,
        'users': user,
    }

    return render(request, 'index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'
