from . import views
from django.urls import paths


urlpatterns = [
    path('', views.PostList.as_view(), name='home')
]
