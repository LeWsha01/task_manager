from django.contrib import admin
from django.urls import path
from django.views import generic

from dashboard import views

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'simple-view',
        views.simple_view,
    ),
    path(
        'about/',
        generic.TemplateView.as_view(template_name='about.html')
    ),
    path(
        'about/<str:page>/',
        views.dynamic_template_view
    ),

    # projects
    path(
        'projects/',
        views.ProjectListView.as_view(),
        name='projects-list'
    ),
    path(
        'projects/<int:pk>/',
        views.ProjectDetailView.as_view(),
        name='projects-detail'
    ),
    path(
        'projects/create/',
        views.ProjectCreateView.as_view(),
        name='projects-create'
    ),
    path(
        'projects/<int:pk>/update/',
        views.ProjectUpdateView.as_view(),
        name='projects-update'
    ),
    path(
        'projects/<int:pk>/delete/',
        views.ProjectDeleteView.as_view(),
        name='projects-delete'
    ),
    path(
        'solar-system',
        views.SolarSystemView.as_view(),
        name='solar-system',
    ),
]
