from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Note
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home_redirect(request):
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("note_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, "note_list.html", {"notes": notes})

class NoteCreateView(CreateView):
    model = Note
    fields = ["title", "content"]
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UpdateView):
    model = Note
    fields = ["title", "content"]
    success_url = reverse_lazy("note_list")

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note_list")
