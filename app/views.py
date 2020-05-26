from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from django.http import JsonResponse


class IndexView(ListView):
    model = Blog
    template_name = "app/index.html"


def addblog(request):
    title = request.POST.get('title')

    blog = Blog()
    blog.title = title
    blog.save()

    d = {
        'title': title,
    }
    return JsonResponse(d)

def searchblog(request):
    title = request.GET.get('title')

    if title:
        title_list = [blog.title for blog in Blog.objects.filter(title__icontains=title)]
    else:
        title_list = [blog.title for blog in Blog.objects.all()]

    d = {
        'title_list': title_list,
    }
    return JsonResponse(d)
