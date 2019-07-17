from django.views.generic import CreateView, ListView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class SubPostListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'post_list.html'


class SubAgent(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'main.html'
    fields = ['choice', 'text', 'post_dates']
    success_url = '/'


def completeTodo(request, todo_id):
    todo = Post.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('post_list')


def uncompleteTodo(request, todo_id):
    todo = Post.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()
    return redirect('post_list')


def deleteCompleted(request):
    Post.objects.filter(complete__exact=True).delete()
    return redirect('post_list')


def deleteAll(request):
    Post.objects.all().delete()
    return redirect('post_list')
