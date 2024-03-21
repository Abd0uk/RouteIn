from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('', views.GoalsListView.as_view(), name='list_goals'), #List all
    path('create/', views.GoalsCreateView.as_view(), name='create_goal'), # create
    path('<int:pk>/', views.GoalsDetailView.as_view(), name='goal_detail'), # list 1
    path('<int:pk>/update', views.GoalsUpdateView.as_view(), name='update_goal'), # update
    path('<int:pk>/delete', views.GoalsDeleteView.as_view(), name='delete_goal'), # delete
    
]
