from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from users.forms import TechUserCreationForm, TechUserUpdateForm, CouponForm
from users.models import TechUser


def registration(request: HttpRequest) -> HttpResponse:
    form = TechUserCreationForm()

    if request.method == "POST":
        form = TechUserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            messages.success(
                request,
                "Thanks for registering. You are now logged in."
            )
            return HttpResponseRedirect(reverse_lazy("note:index"))

    return render(request, 'registration/sign_up.html', {'form': form})


class TechUserDetailView(LoginRequiredMixin, generic.DetailView):
    queryset = TechUser.objects.prefetch_related("note_groups")
    template_name = "users/tech_user_detail.html"


class TechUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TechUser
    template_name = "users/tech_user_form.html"
    form_class = TechUserUpdateForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)


class TechUserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TechUser
    template_name = "users/tech_user_confirm_delete.html"
    success_url = reverse_lazy("note:index")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)


@login_required
def coupon_code_view(request: HttpRequest, pk: int) -> HttpResponse:
    form = CouponForm()

    if request.method == "POST":
        form = CouponForm(request.POST)

        if form.is_valid():
            messages.success(request, "Thanks! Here is your gift!")
            return render(request, 'users/coupon_code_gift.html')

    return render(request, 'users/coupon_code_form.html', {'form': form})
