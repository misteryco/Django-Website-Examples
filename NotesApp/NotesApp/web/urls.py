from django.urls import path

from NotesApp.web.views import home_page, edit_note, add_note, delete_note, details_note, profile_create, profile_view, \
    profile_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='note details'),

    path('profile/create/', profile_create, name='profile create'),
    path('profile/', profile_view, name='profile view'),
    path('profile/<int:pk>/', profile_delete, name='profile delete'),
]
