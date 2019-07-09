from django.urls import path
from .views import SubPostListView, SubAgent

urlpatterns = [
    path('', SubPostListView.as_view(), name='post_list'),
    path('create/', SubAgent.as_view(), name='main'),
]