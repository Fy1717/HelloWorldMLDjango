from django.shortcuts import render, HttpResponse , get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request):
    return HttpResponse('Burası POST  detail Sayfası')

def post_create(request):    
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
    else:
        form = PostForm()

    context = {
        'form': form,
    } 

    return render(request, 'post/form.html', context)

def post_update(request):
    return HttpResponse('Burası POST  update Sayfası')  

def post_delete(request):
    return HttpResponse('Burası POST  delete Sayfası')