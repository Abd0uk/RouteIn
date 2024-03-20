from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    # path('', views.GoalsListView.as_view(), name='list_goals'), List all
    path('create', views.GoalsCreateView.as_view(), name='create_goal'), # create
    # path('create', views.GoalsCreateView.as_view(), name='create_goal'), # list 1
    # path('create', views.GoalsCreateView.as_view(), name='create_goal'), # update
    # path('create', views.GoalsCreateView.as_view(), name='create_goal'), # delete
    
]
