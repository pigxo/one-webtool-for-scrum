from django.conf.urls import url
from robotcase import views


urlpatterns = [
    url(r'^download/(?P<case_name>.+)/$', views.file_download, name='case_download'),
    url(r'^index/$', views.IndexView.as_view(), name='robotcase_index'),

]
