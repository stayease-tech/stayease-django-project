from django.views.generic import TemplateView
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('normal-enquiry/', views.normal_enquiry, name='normal_enquiry'),
    path('visit-enquiry/', views.visit_enquiry, name='visit_enquiry'),
    re_path(r'^.*$', TemplateView.as_view(template_name='stayease_app/index.html')),
]
