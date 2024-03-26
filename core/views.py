from django.shortcuts import render
from .models import booksDataBase
from.forms import insertBook
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def home(request):
    template_name='core/home.html'
    return render(request, template_name)

def search(request):
    template_name='core/search.html'
    return render(request, template_name)

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