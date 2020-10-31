from django.shortcuts import render
from django.http import HttpResponse
from .models import teach_prof

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages

# class AddTutorView(LoginRequiredMixin, CreateView):
#     model = teach_prof
#     fields = ['name', 'teach_class', 'lang', 'Subj', 'city', 'state','Email','contact']
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

class TutorListView(LoginRequiredMixin, ListView):
    model = teach_prof
    template_name = 'cars/cars.html' ####main student page
    context_object_name = 'Tutor'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            name_results = self.model.objects.filter(
                user=self.request.user, name=q).order_by('-pk')
            subj_results = self.model.objects.filter(
                user=self.request.user, Subj=q).order_by('-pk')
            city_results = self.model.objects.filter(
                user=self.request.user, city=q).order_by('-pk')
            state_results = self.model.objects.filter(
                user=self.request.user, state=q).order_by('-pk')
            if name_results.exists():
                return name_results
            elif subj_results.exists():
                return subj_results
            elif city_results.exists():
                return city_results
            elif state_results.exists():
                return state_results
            else:
                return self.model.objects.none()
        return self.model.objects.filter(user=self.request.user).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

class UpdateTutorView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = teach_prof
    fields = ['name', 'teach_class', 'lang', 'Subj', 'city', 'state','Email','contact']
    success_message = 'Tutor details has been updated!'

    def get_success_url(self, **kwargs):
        row = self.request.GET.get('row')
        p = self.request.GET.get('p')
        q = self.request.GET.get('q')
        options = '?p=' + p + '&row=' + row
        options += '&q=' + q
        messages.success(self.request, self.success_message)
        return reverse_lazy('tutor_detail') + options

    def test_func(self):
        if self.get_object().user == self.request.user:
            return True
        return False

class DeleteTutorView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = teach_prof
    success_url = '/'

    def test_func(self):
        if self.get_object().user == self.request.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        success_message = f'The Tutor {self.get_object()} details has been deleted!'
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)




















##dummy data
message= [
    {
        'sender':'sak',
        'reciever': 'asfia',
        'start_date': 'aaj',
    }
]
def myHome(request):
    return HttpResponse("<h1>hsgygf</h1>")

def logopage(request):
    return render(request, 'learn/logopage.html')  ##working

def myMat(request):
    context = {
        'message': message
    }
    return render(request, 'learn/ghar.html', context)
