from django.urls import path

from djangoProject_exam.web import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
]
