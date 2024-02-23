from django.urls import path

from exam_prep.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailsView.as_view(), name='profile_details'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete_profile'),
]
