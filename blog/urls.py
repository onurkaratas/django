from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog' , views.post_list, name="post_list"),
    url(r'^cripto', views.cripto_app, name="cripto"),
    url(r'^hello', views.hello, name="hello"),
    url(r'^git-guide', views.git_guide, name="git-guide")
]