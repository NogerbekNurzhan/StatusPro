from django.conf.urls import url
from video.views import (
    TelevisionProgramListView,
    TelevisionProgramDetailView,
)

urlpatterns = [
    url(
        r'^television_program/',
        TelevisionProgramListView.as_view(),
        name='television_program_list',
    ),
    url(
        r'^television_program/(?P<pk>\d+)/$',
        TelevisionProgramDetailView.as_view(),
        name='television_program_detail'
    ),
]
