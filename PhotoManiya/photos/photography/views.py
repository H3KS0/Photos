from django.shortcuts import render
from photography.models import PhotoCategory, Post, Like, Pictures
# Create your views here.
def Menu (request):
    context = {
        'title': 'Menu',
        'categorys':PhotoCategory.objects.all(),
        'posts': Post.objects.all()
        }
    return render(request, 'photography/Menu.html', context)

def Photo (request):
    context = {
        'title': 'Photo',
        'categorys': PhotoCategory.objects.all(),
        'pictures': Pictures.objects.all(),
        'likes': Like.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'photography/Photo.html', context)