from django.shortcuts import render
from .models import Poll


def index(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/index.html', context)
