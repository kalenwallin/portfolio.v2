from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('init/', views.init.as_view(), name='init'),
    path('', views.index, name='index'),
    path('<slug:slug>/', views.page.as_view(), name='page'),
]
