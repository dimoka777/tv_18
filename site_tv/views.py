from django.views.generic import CreateView, ListView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class SubPostListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'post_list.html'


class SubAgent(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'main.html'
    fields = ['choice', 'text', 'post_dates']
    success_url = '/'
