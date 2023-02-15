from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<slug:slug>/', views.page.as_view(), name='page'),
    path('like/<int:id>', views.page_heart, name='page_heart'),
]