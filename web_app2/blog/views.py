from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Post, PostAttachFile
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic import FormView
from django.db.models import Q
from django.shortcuts import render
from blog.forms import PostSearchForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
import os
from django.conf import settings


# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 템플릿 파일명 변경
    context_object_name = 'posts'  # 컨텍스트 객체 이름 변경(object_list)
    paginate_by = 2  # 페이지네이션, 페이지당 문서 건 수

    def get_context_data(self, **kwargs):
        context = super(PostLV, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


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


# --- Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user

        response= super().form_valid(form) # Post모델 저장, self.object

        # 업로드 파일 얻기
        files=self.request.FILES.getlist("files")
        for file in files:
            attach_file=PostAttachFile(post=self.object,filename=file.name, size=file.size,content_type=file.content_type,upload_file=file)
            attach_file.save()
        return response


class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files: # fid는 문자열 타입임
            file = PostAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path) # 실제 파일 삭제
            file.delete() # 모델 삭제(테이블의 행 삭제)

        response = super().form_valid(form)
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = PostAttachFile(post= self.object, filename = file.name,size = file.size, content_type = file.content_type, upload_file = file)
            attach_file.save()
        return response
    
class PostDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('blog:index')


def download(request, id):
    file = PostAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))

    return FileResponse(open(file_path, 'rb'))