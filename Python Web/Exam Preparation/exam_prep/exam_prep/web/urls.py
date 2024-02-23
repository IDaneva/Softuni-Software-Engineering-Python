from django.urls import path, include

from exam_prep.web import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-profile", views.create_profile, name="create_profile"),
]
