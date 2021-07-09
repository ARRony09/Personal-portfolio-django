from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('', views.blogList,name='blogList'),
    path('<int:blog_id>', views.details,name='details')
]