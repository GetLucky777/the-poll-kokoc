from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .forms import CreationForm, ChangeColorForm
from .models import Colors


def profile(request):
    form = ChangeColorForm(
        request.POST or None,
        files=request.FILES or None,
        instance=request.user
    )
    if form.is_valid():
        login_color = form.cleaned_data['login_color']
        backgrnd_color = form.cleaned_data['background_color']
        request.user.balance -= Colors.objects.get(color=login_color).cost
        request.user.balance -= Colors.objects.get(color=backgrnd_color).cost
        form.save()
    return render(request, 'users/profile.html', {'form': form})


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('polls:index')
    template_name = 'users/signup.html' 
