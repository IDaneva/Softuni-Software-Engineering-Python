from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

from exam_prep.profiles.models import Profile


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "templates/profile-details.html"

    def get_object(self, queryset=None):
        return Profile.objects.first()


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "templates/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return Profile.objects.first()
