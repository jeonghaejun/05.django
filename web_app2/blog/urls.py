from django.urls import path, re_path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    # re_path(r'^(?P<slug>[-\w]+)/$', PostDV.as_view(), name='detail'),
    path('<int:pk>/', PostDV.as_view(), name='detail'),
]
