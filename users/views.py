from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView

from users.forms import TechUserCreationForm
from users.models import TechUser


def registration(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TechUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/")

    form = TechUserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


class TechUserDetailView(LoginRequiredMixin, DetailView):
    model = TechUser
    template_name = "users/tech_user_detail.html"
