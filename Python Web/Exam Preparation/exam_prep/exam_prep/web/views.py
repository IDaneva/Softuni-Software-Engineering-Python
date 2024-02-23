from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.forms import ModelForm

from exam_prep.profiles.models import Profile
from exam_prep.albums.models import Album
from django.views import generic as views


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {"form": form}

    return render(request, 'templates/home-no-profile.html', context)


def index(request):
    profile = Profile.objects.first()

    if not profile:
        return create_profile(request)

    albums = profile.albums.all()

    context = {"albums": albums}
    return render(request, 'templates/home-with-profile.html', context)




