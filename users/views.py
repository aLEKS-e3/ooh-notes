from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from users.forms import TechUserCreationForm


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
