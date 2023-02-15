from django.shortcuts import render
from django.views import generic
from .models import Row, Page, Lover


def index(request):
    rows = Row.objects.order_by('order')
    context = {'rows': rows}
    return render(request, 'portfolio/portfolio.html', context)

def fappy_borbs(request):
    return render(request, 'portfolio/fappy_borbs/fappy_borbs.html')

# Hearting code modified from here: https://www.youtube.com/watch?v=AZwc9hDBi04

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class page(generic.DetailView):
    model = Page
    template_name = 'portfolio/page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ip = get_client_ip(self.request)
        if Lover.objects.filter(ip=ip).exists():
            context['ip'] = Lover.objects.filter(ip=ip).first()
        return context

def page_heart(request, id):
    if request.method == "POST":
        instance = Page.objects.get(id=id)
        ip = get_client_ip(request)
        if not Lover.objects.filter(ip=ip).exists():
            lover = Lover.objects.create(ip=ip)
        else:
            lover = Lover.objects.filter(ip=ip).first()

        if not instance.hearts.filter(id=lover.id).exists():
            instance.hearts.add(lover)
            instance.save()
            context = {'page': instance, 'ip': lover}
            return render(request, 'portfolio/page_heart.html', context)
        else:
            instance.hearts.remove(lover)
            instance.save()
            context = {'page': instance, 'ip': lover}
            return render(request, 'portfolio/page_heart.html', context)