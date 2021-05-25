from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('blog/post', postRequest),
    path('blog/edit', updateRequest),
    path('blog/delete', deleteRequest),
]