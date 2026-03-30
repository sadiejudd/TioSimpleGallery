from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Image

# Create your views here.

class UploadView(CreateView):
    model = Image
    fields = ["image"]
    template_name = "gallery/upload.html"
    success_url = "/home"

    def from_valid(self, form):
        if not self.request.session.session_key:
            self.request.session.create()

        form.instance.session_id = self.request.session.session_key
        return super().form_valid(form)


class HomeView(ListView):
    model = Image 
    template_name = "gallery/home.html"
    context_object_name = "images"
