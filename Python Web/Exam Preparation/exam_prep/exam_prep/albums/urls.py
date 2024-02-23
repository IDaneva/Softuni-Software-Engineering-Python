from django.urls import path, include

from exam_prep.albums import views

urlpatterns = [
    path('add/', views.CreateAlbumView.as_view(), name='create_album'),
    path('<int:pk>', include([
        (path('details/', views.DetailAlbumView.as_view(), name='album_details')),
        (path('edit/', views.EditAlbumView.as_view(), name='edit_album')),
        (path('delete/', views.DeleteAlbumView.as_view(), name='delete_album')),
    ]))
]
