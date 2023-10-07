from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('post/<str:pk>', views.post, name='post'),
    path('latest-posts/', views.latestPosts, name='latest-posts'),
    path('test/', views.test, name='test')
]

