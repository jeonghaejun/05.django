from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView


# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 템플릿 파일명 변경
    context_object_name = 'posts'  # 컨텍스트 객체 이름 변경(object_list)
    paginate_by = 2  # 페이지네이션, 페이지당 문서 건 수


# DetailView
class PostDV(DetailView):
    model = Post

# ArchiveView


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'
