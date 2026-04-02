from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Image, Tag, Comment
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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]







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

        recent_ids = self.request.session.get("recent_images", [])
        recent_images = Image.objects.filter(id__in = recent_ids)
        recent_images = sorted(recent_images, key=lambda x: recent_ids.index(x.id))
        

        context= super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["recents"] = recent_images
        return context
    

class ImageDetailView(DetailView):
    model = Image
    template_name = "gallery/detail.html"
    context_object_name = "image"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        recent = request.session.get("recent_images", [])

        image_id = self.object.id

        if(id in recent):
            recent.remove(id)

        recent.insert(0, image_id)
        recent = recent[:5]

        request.session["recent_images"] = recent




        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        comments_ = Comment.objects.all()
        context = super().get_context_data(**kwargs)
        context["comments"] = comments_
        context["form"] = CommentForm()

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = CommentForm(request.POST)

        if form.is_valid():
           form.save()



        context = self.get_context_data()
        

        return self.render_to_response(context)

        


    
    
    


    
