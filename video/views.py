from video.models import Video
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class TelevisionProgramListView(ListView):
    model = Video
    template_name = 'television_program_list.html'
    context_object_name = 'video'
    paginate_by = 9
    queryset = Video.objects.filter(category_id=1)


class TelevisionProgramDetailView(DetailView):
    model = Video
    template_name = 'television_program_detail.html'
    context_object_name = 'video'
