from django import http, urls
from django import template
from django import shortcuts
from django.views import generic

from dashboard import models


def simple_view(request):
    return http.HttpResponse('<h1>Hello, world!</h1>')


def dynamic_template_view(request, page):
    try:
        return shortcuts.render(request, f'about/{page}.html')
    except template.TemplateDoesNotExist:
        raise http.Http404()


class ProjectListView(generic.ListView):
    model = models.Project
    template_name = 'project_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Project.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count'] = models.Project.objects.count()
        return context_data


class ProjectDetailView(generic.DetailView):
    model = models.Project
    template_name = 'project_detail.html'


class ProjectCreateView(generic.CreateView):
    model = models.Project
    fields = [
        'name',
        'description',
    ]
    template_name = 'project_create.html'


class ProjectUpdateView(generic.UpdateView):
    model = models.Project
    fields = [
        'name',
        'description',
    ]
    template_name = 'project_update.html'


class ProjectDeleteView(generic.DeleteView):
    model = models.Project
    success_url = urls.reverse_lazy('projects-list')
    template_name = 'project_delete.html'


class SolarSystemView(generic.TemplateView):
    template_name = 'solar-system.html'
