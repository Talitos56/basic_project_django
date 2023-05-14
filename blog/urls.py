from django.urls import path

from . import views

app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/
urlpatterns = [
    path('<int:id>/', views.post, name='post'),
    path('', views.blog, name='home'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
