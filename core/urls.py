from django.urls import path
from .views import home_redirect, register_view, login_view, logout_view, note_list, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path("", home_redirect, name="home"),   
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("notes/", note_list, name="note_list"),
    path("notes/add/", NoteCreateView.as_view(), name="note_add"),
    path("notes/<int:pk>/edit/", NoteUpdateView.as_view(), name="note_edit"),
    path("notes/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
]
