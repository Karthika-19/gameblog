from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
    return render(request, 'myblog/index.html',{'posts':posts})

