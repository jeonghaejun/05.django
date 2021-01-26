from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV
app_name = 'bookmark' # 해당 애플리케이션의 네임스페이스명
urlpatterns = [
path('', BookmarkLV.as_view(), name='index'),
path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]