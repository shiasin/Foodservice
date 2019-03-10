from django.conf.urls import url
from kitchen import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]