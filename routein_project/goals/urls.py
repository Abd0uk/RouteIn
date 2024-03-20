from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('create', views.GoalsCreateView.as_view(), name='create_goal')
]
