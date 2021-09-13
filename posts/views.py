from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):


    #If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST )
        # If the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')

            #No, show error
        else:
            return HttpResponseRedirect(form.erros.as_json())



    posts = Post.objects.all()[:20]


    return render(request, 'posts.html',
                {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')