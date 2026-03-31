from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Image, Tag
from django.urls import reverse_lazy
from django import forms

# Create your views here.

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple()
        }




class UploadView(CreateView):
    model = Image
    form_class = ImageForm
    template_name = "gallery/upload.html"
    success_url = reverse_lazy("home")

  

    def form_valid(self, form):
        if not self.request.session.session_key:
            self.request.session.create()

        form.instance.session= self.request.session.session_key
        return super().form_valid(form)


class HomeView(ListView):
    model = Image
    template_name = "gallery/home.html"
    context_object_name = "images"

    def get_queryset(self):
        if not self.request.session.session_key:
            self.request.session.create()


        query_set = super().get_queryset()
        query_set = query_set.filter(session = self.request.session.session_key)

        selected_tags = self.request.GET.getlist("tags")

        if selected_tags:
            query_set = query_set.filter(tags__id__in=selected_tags).distinct()
        
        return query_set

    
    
    
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
    
