from django.urls import path
from djangoProject_exam.user_profile import views

urlpatterns = [
    path("create/", views.CreateProfileView.as_view(), name="create_profile"),
    path("details/", views.DetailProfileView.as_view(), name="profile_details"),
    path("edit/", views.EditProfileView.as_view(), name="edit_profile"),
    path("delete/", views.DeleteProfileView.as_view(), name="delete_profile"),
]
