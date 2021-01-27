from django.urls import path, re_path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    # re_path(r'^(?P<slug>[-\w]+)/$', PostDV.as_view(), name='detail'),
    path('<int:pk>/', PostDV.as_view(), name='detail'),
    # Example: /blog/archive/
    path('archive/', PostAV.as_view(), name='post_archive'),
    # Example: /blog/archive/2019/
    path('archive/<int:year>/', PostYAV.as_view(),name='post_year_archive'),
    # Example: /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', PostMAV.as_view(),name='post_month_archive'),
    # Example: /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', PostDAV.as_view(),name='post_day_archive'),
    # Example: /blog/archive/today/
    path('archive/today/', PostTAV.as_view(), name='post_today_archive'),
]
