from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# from django.urls import reverse_lazy

class NewDatailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'articles'


class MultipleSubminMixin:
    error = ''
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        form = self.get_form()
        if action == 'delete':
            self.object = self.get_object()
            self.object.delete()
            return HttpResponseRedirect(f'/')
        if action == 'update':
            if form.is_valid():
                return super().post(request, *args, **kwargs)
            else:
                errors = "Form is not valid"
                return HttpResponseRedirect(f'/{self.get_object().id}/update', errors)



class ItemUpdateDeleteView(MultipleSubminMixin, UpdateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'news/update_delete.html'


# class NewUpdateView(UpdateView):
#     model = Articles
#     template_name = 'news/update_delete.html'
#     form_class = ArticlesForm


class NewDeleteView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


def news_home(request):
    news = Articles.objects.all().order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = "Форма введена неверно "
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    error = ''
    return render(request, 'news/create.html', data)
