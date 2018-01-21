from django.conf.urls import url, include
from grooming import views


urlpatterns = [
    url(r'^index/search/', include('haystack.urls')),
    url(r'^detail/(?P<grooming_id>\d+)/$', views.GroomingDetailView.as_view(), name='grooming_detail'),
    url(r'^index/$',views.GroomingIndexView.as_view(), name='grooming_index'),
    url(r'^create/$',views.GroomingCreateView.as_view(),name='grooming_create'),
    url(r'^newatdd/$',views.AddATDDView.as_view(), name='grooming_add_atdd'),
    url(r'^detail/(?P<grooming_id>\d+)/newatdd/$',views.AddATDDView.as_view(),name='grooming_edit_atdd'),
    url(r'^detail/atdd/(?P<atdd_id>\d+)/$', views.add_atdd, name='grooming_atdd_detail'),
    url(r'^detail/(?P<grooming_id>\d+)/edit/$', views.GroomingDetailEditView.as_view(), name='grooming_detail_eidt'),
    url(r'^feature/index/$',views.FeatureIndexView.as_view(), name='feature_index'),
]
