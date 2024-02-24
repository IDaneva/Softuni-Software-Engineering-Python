from django.urls import path, include

from djangoProject_exam.car import views

urlpatterns = [
    # path("catalogue/", views.ViewCarCatalogue.as_view(), name="view_catalogue"),
    path("create/", views.CreateCarView.as_view(), name="create_car"),
    path("catalogue/", views.view_car_catalogue, name="view_catalogue"),
    path("<int:pk>/", include([
        (path("details/", views.DetailCarView.as_view(), name="car_details")),
        (path("edit/", views.EditCarView.as_view(), name="edit_car")),
        (path("delete/", views.DeleteCarView.as_view(), name="delete_car")),
    ]))
]