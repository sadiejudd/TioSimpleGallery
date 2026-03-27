from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Image
from django.urls import reverse_lazy

# Create your views here.

class UploadView(CreateView):
    model = Image
    fields = ["image"]
    template_name = "gallery/upload.html"
    success_url = reverse_lazy("home")


class HomeView(ListView):
    model = Image 
    template_name = "gallery/home.html"
    context_object_name = "images"
