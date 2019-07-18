from django.urls import path
from .views import *

urlpatterns = [
    path('', SubPostListView.as_view(), name='post_list'),
    path('create/', addTodo, name='main'),
    path('complete/<todo_id>', completeTodo, name='complete'),
    path('uncomplete/<todo_id>', uncompleteTodo, name='uncomplete'),
    path('deletecomplete', deleteCompleted, name='deletecomplete'),
    path('deleteall', deleteAll, name='deleteall'),
]
