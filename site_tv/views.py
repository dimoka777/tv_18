from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView
from site_tv.forms import CreateField
from .models import Post, Choice
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render


class SubPostListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'post_list.html'


class SubAgent(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'main.html'
    fields = ['choice', 'text', 'post_dates']
    success_url = '/'


def test(request):
    test_create = Post.objects.order_by('id')
    form = CreateField()
    context = {'test_create': test_create, 'form': form}
    return render(request, 'test.html', context)


def addTodo(request):
    form = CreateField
    if request.method == 'POST':
        form = CreateField(request.POST)
        if form.is_valid():
            a = request.POST['date']
            c = request.POST['text']
            b = request.POST['choice']
            post=Post.objects.create(
                 post_dates=a, text=c, choice=Choice.objects.get(pk=b)
             )
            post.save()
            # return render(request, 'test.html', {'form': post})
            return redirect('post_list')
        else:
            print('ERROR')
    return render(request, 'main.html', {'form': form})
 

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
