from django.urls import path,re_path
from .views import AppView


urlpatterns = [
    re_path(r'^.*/$',AppView.as_view(),name='any_other')
]