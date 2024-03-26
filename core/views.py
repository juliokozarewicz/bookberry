from django.shortcuts import render
from .models import booksDataBase
from.forms import insertBook
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def home(request):
    template_name='core/home.html'
    return render(request, template_name)

@method_decorator(login_required, name='dispatch')
class search(CreateView):
    model = booksDataBase
    form_class = insertBook
    template_name = 'core/search.html'
    context_object_name = 'search_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_list'] = booksDataBase.objects.filter(user=self.request.user).order_by('bookname')
        context['total_books'] = len(booksDataBase.objects.filter(user=self.request.user).order_by('bookname'))
        return context

    def get_queryset(self):
        return Table_invoices.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class insert(CreateView):
    model = booksDataBase
    form_class = insertBook
    template_name = 'core/insert.html'
    context_object_name = 'insert'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class delete(DeleteView):
    model = booksDataBase
    success_url = reverse_lazy('core:search')
    template_name = 'core/search.html'