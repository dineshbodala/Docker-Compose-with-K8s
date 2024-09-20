from django.urls import path, re_path
from . import views

urlpatterns = [
    # For the homepage, replace url() with path()
    path('', views.index, name='index'),

    # For the URL with a regular expression, replace url() with re_path()
    re_path(r'^details/(?P<id>\w{0,50})/$', views.details),

    # For the 'add' URL, replace url() with path()
    path('add', views.add, name='add'),
]
