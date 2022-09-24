from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test',views.test),
    path('<int:id>/results/',views.dyn),
    path('tail',views.tail)
]