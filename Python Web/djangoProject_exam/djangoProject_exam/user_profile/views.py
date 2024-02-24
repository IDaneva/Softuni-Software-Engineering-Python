from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms

from djangoProject_exam.user_profile.models import Profile


class CreateProfileView(views.CreateView):
    queryset = Profile.objects.all()
    fields = ("username", "email", "age", "password")
    template_name = "html_templates/profile/profile-create.html"
    success_url = reverse_lazy("view_catalogue")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['password'].widget = forms.PasswordInput()
        form.fields['age'].help_text = "Age requirement: 21 years and above."
        return form


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "html_templates/profile/profile-details.html"

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        cars = profile.car_set.all()
        total_price = sum(car.price for car in cars)
        context["total_price"] = total_price
        return context


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "html_templates/profile/profile-edit.html"
    fields = ("username", "email", "age", "password", "first_name", "last_name", "profile_picture")
    success_url = reverse_lazy("profile_details")

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['age'].help_text = "Age requirement: 21 years and above."
        return form


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "html_templates/profile/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return Profile.objects.first()

