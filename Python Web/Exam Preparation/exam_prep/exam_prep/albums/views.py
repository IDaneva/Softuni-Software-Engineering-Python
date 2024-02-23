from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

from exam_prep.albums.models import Album
from exam_prep.profiles.models import Profile


class CreateAlbumView(views.CreateView):
    queryset = Album.objects.all()
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    template_name = "templates/album-add.html"
    success_url = reverse_lazy("index")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['name'].widget.attrs['placeholder'] = "Album name"
        form.fields['artist_name'].widget.attrs['placeholder'] = "Artist name"
        form.fields['genre'].widget.attrs['placeholder'] = "Genre"
        form.fields['description'].widget.attrs['placeholder'] = "Description"
        form.fields['image_url'].widget.attrs['placeholder'] = "Image Url"
        form.fields['price'].widget.attrs['placeholder'] = "Price"
        return form

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = Profile.objects.first()
        return super().form_valid(form)


class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'templates/album-details.html'


class EditAlbumView(views.UpdateView):
    queryset = Album.objects.all()
    template_name = 'templates/album-edit.html'
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    success_url = reverse_lazy("index")


class DeleteAlbumView(views.DeleteView):
    queryset = Album.objects.all()
    template_name = 'templates/album-delete.html'
    success_url = reverse_lazy("index")
    form_class = modelform_factory(
        Album,
        fields=['name', 'artist_name', 'genre', 'description', 'image_url', 'price'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
        return form
