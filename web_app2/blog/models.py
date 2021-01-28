from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):

    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,
                            help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100,
                                   blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:

        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'  # 테이블명 재정의
        ordering = ('-modify_dt',)  # orderby 절, -이면 내림차순

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # 현재 데이터의 절대 경로 추출
        # return reverse('blog:detail', args=(self.slug,))
        return reverse('blog:detail', args=(self.id,))

    def get_previous(self):  # 이전 데이터 추출
        return self.get_previous_by_modify_dt()

    def get_next(self):  # 다음 데이터 추출
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
