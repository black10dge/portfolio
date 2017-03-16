from django.shortcuts import render
from django.http import HttpResponse

from publication.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "index.html", { "posts": posts })