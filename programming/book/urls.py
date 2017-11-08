from django.conf.urls import url
from . import views
from .views import (index,add,edit,delete,view)

urlpatterns = [
    url(r'^$', index, name="book"),
    url(r'^add', add, name="addbook"),
    url(r'^edit/(?P<id>.+)$', views.edit, name="editbook"),
    url(r'^view/(?P<id>.+)$', views.view, name="viewbook"),
    url(r'^delete/(?P<id>.+)$', views.delete, name="deletebook"),
]