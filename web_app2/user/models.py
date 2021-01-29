# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# from django.db import models

# # Create your models here.


# class MyUserManager(BaseUserManager):
#     def _create_user(self, email, password=None, **kwargs):
#         if not email:
#             raise ValueError('이메일은 필수입니다.')
#         user = self.model(email=self.normalize_email(email), **kwargs)
#         user.set_password(password)
#         user.save(using=self._db)

#     def create_user(self, email, password, **kwargs):
#         """
#         일반 유저 생성
#         """
#         kwargs.setdefault('is_admin', False)
#         return self._create_user(email, password, **kwargs)

#     def create_superuser(self, email, password, **kwargs):
#         """
#         관리자 유저 생성
#         """
#         kwargs.setdefault('is_admin', True)
#         return self._create_user(email, password, **kwargs)

# class MyUser(AbstractBaseUser):
#     # 사용자 ID로 email을 사용
#     email = models.EmailField(unique=True, verbose_name='이메일')
#     name = models.CharField(max_length=20, verbose_name='이름')
#     date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
#     is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
#     is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')

#     # 모델 매니저
#     objects = MyUserManager()

#     class Meta:
#         db_table = 'users'
#         verbose_name = '유저'
#         verbose_name_plural = '유저들'