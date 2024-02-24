from django.forms import modelform_factory
from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from djangoProject_exam.car.models import Car
from djangoProject_exam.user_profile.models import Profile


class ViewCarCatalogue(views.DetailView):
    queryset = Car.objects.all()
    template_name = "html_templates/car/catalogue.html"

    def get_object(self, queryset=None):
        return Profile.objects.first()


class CreateCarView(views.CreateView):
    queryset = Car.objects.all()
    fields = ("type", "model", "year", "image_url", "price")
    template_name = "html_templates/car/car-create.html"
    success_url = reverse_lazy("view_catalogue")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["image_url"].widget.attrs["placeholder"] = "https://..."
        return form

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = Profile.objects.first()
        return super().form_valid(form)


# class ViewCatalogueView(views.TemplateView):
#     template_name = "html_templates/car/catalogue.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         profile = Profile.objects.first()
#         cars = profile.car_set.all()
#         context['profile'] = profile
#         context['cars'] = cars
#         return context


def view_car_catalogue(request):
    profile = Profile.objects.first()
    cars = profile.car_set.all()
    context = {"profile": profile, "cars": cars}
    return render(request, 'html_templates/car/catalogue.html', context)


class DetailCarView(views.DetailView):
    queryset = Car.objects.all()
    template_name = "html_templates/car/car-details.html"


class EditCarView(views.UpdateView):
    queryset = Car.objects.all()
    fields = ("type", "model", "year", "image_url", "price")
    template_name = "html_templates/car/car-edit.html"
    success_url = reverse_lazy("view_catalogue")


class DeleteCarView(views.DeleteView):
    queryset = Car.objects.all()
    template_name = "html_templates/car/car-delete.html"
    success_url = reverse_lazy("view_catalogue")
    form_class = modelform_factory(Car, fields=("type", "model", "year", "image_url", "price"))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field_name, field in form.fields.items():
            if isinstance(field, forms.CharField) and field_name == "type":
                field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True

        return form
