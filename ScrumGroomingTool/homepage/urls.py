from django.conf.urls import url
from homepage import views


urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^index/edit/$',views.IndexDetailView.as_view(),name='index_detail'),]