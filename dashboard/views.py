from django import http, urls
from django import template
from django import shortcuts
from django.contrib.auth import decorators, mixins
from django.views import generic

from dashboard import models, forms


def simple_view(request):
    return http.HttpResponse('<h1>Hello, world!</h1>')


def dynamic_template_view(request, page):
    try:
        return shortcuts.render(request, f'about/{page}.html')
    except template.TemplateDoesNotExist:
        raise http.Http404()


class AboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = [
            {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
            {'name': 'Calcutta', 'population': '15,000,000',
             'country': 'India'},
            {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
            {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
            {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
        ]
        return context


class ProjectListView(mixins.LoginRequiredMixin, generic.ListView):
    model = models.Project
    template_name = 'project_list.html'
    paginate_by = 5
    login_url = '/login/'

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
        'logo',
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


class ContactUsView(generic.FormView):
    form_class = forms.ConstuctUsForm
    template_name = 'contact_us.html'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        recipients = [form.cleaned_data['email']]
        # send_mail(subject, message, sender, recipients)
        return http.HttpResponseRedirect('/projects/')
