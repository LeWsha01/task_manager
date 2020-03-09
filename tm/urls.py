from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from authentication import views as auth_views
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
        views.AboutView.as_view(),
        name='about',
    ),
    path(
        'about/<str:page>/',
        views.dynamic_template_view
    ),

    # auth
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
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
        'contact-us/',
        views.ContactUsView.as_view(),
        name='contact-us'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

