from django.urls import path


from .views import *
from . import views


# app_name = 'articles'
urlpatterns = [
    path('', index, name='home'),
    path('about_all/', about_all, name='about_all'),
    path('development/', development, name='development'),
    path('administration/', administration, name='administration'),
    path('design/', design, name='design'),
    path('management/', management, name='management'),
    path('marketing/', marketing, name='marketing'),
    path('science/', science, name='science'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),




]