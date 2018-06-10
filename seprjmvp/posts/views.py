from django.shortcuts import render

from .models import Posts


# Create your views here.


def index(request):
    # return HttpResponse('Hello From Posts.')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Please Login',
        'posts': posts,
    }

    return render(request=request, template_name='posts/index.html', context=context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request=request, template_name='posts/details.html', context=context)
