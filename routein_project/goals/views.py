from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Goals
from .forms import GoalsForm
# Create your views here.

class GoalsCreateView(CreateView):
    model = Goals
    template_name = 'goals_form.html'
    form_class = GoalsForm
    # context_object_name = 'goal'
    success_url = reverse_lazy('goals:goal_detail')

    def form_valid(self, form):
        # Save the form instance along with the user who submitted it
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('goals:goal_detail', kwargs={'pk': self.object.pk})


class GoalsDetailView(DetailView):
    model = Goals
    template_name = 'goal_detail.html'


class GoalsListView(ListView):
    model = Goals
    template_name = "goals_list.html"

class GoalsUpdateView(UpdateView):
    model = Goals
    form_class = GoalsForm
    template_name = 'goal_update.html'
    success_url = reverse_lazy('goals:goal_detail')
    
    def get_success_url(self):
        return reverse_lazy('goals:goal_detail', kwargs={'pk': self.object.pk})

class GoalsDeleteView(DeleteView):
    model = Goals
    template_name = 'goal_confirm_delete.html'
    success_url = reverse_lazy('goals:list_goals')