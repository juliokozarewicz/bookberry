from django.shortcuts import render
from .models import booksDataBase
from.forms import insertBook
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

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

    message_ok ='Livro inserido no sistema.'
    messade_erro = 'Não foi possível realizar a tarefa!'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.add_message(self.request, messages.INFO, self.message_ok)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class delete(DeleteView):
    model = booksDataBase
    success_url = reverse_lazy('core:search')
    template_name = 'core/search.html'

    message_ok ='Livro apagado do sistema.'
    messade_erro = 'Não foi possível realizar a tarefa!'

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, self.message_ok)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class edit(UpdateView):
    model = booksDataBase
    form_class = insertBook
    template_name = 'core/edit.html'
    context_object_name = 'edit'

    message_ok ='Livro editado com sucesso.'
    messade_erro = 'Não foi possível realizar a tarefa!'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.add_message(self.request, messages.INFO, self.message_ok)
        return super().form_valid(form)