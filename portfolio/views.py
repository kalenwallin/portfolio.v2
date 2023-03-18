from django.shortcuts import render
from django.views import generic
from .models import Category, Article


def index(request):
    rows = Category.objects.order_by('order')
    context = {'rows': rows}
    return render(request, 'portfolio/portfolio.html', context)


def fappy_borbs(request):
    return render(request, 'portfolio/fappy_borbs/fappy_borbs.html')


class page(generic.DetailView):
    model = Article
    template_name = 'portfolio/page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context
