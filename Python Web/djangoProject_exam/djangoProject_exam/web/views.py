from django.shortcuts import render
from djangoProject_exam.user_profile.models import Profile


def index(request):
    return render(request, "html_templates/index.html",)

