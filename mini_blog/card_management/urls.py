from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('blog/post', postRequest),
    path('blog/<int:blog_id>/edit', updateRequest),
    path('blog/<int:blog_id>/delete', deleteRequest),
]