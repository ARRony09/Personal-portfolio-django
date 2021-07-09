from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.

def blogList(request):
    post=Post.objects.order_by('-date')
    return render(request,'blog/blog_list.html',{'allposts':post})

def details(request,blog_id):
    blog=get_object_or_404(Post,pk=blog_id)
    return render(request,"blog/details.html",{'blog':blog})