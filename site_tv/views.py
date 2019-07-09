from django.views.generic import CreateView, ListView
from .models import Post


class SubPostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class SubAgent(CreateView):
    model = Post
    template_name = 'main.html'
    fields = ['tv_choice', 'text', 'post_dates']
    success_url = '/'


