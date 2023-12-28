from django.urls import path
from dashboard.admin import staff_dashboard_site
from frontend.views import index

urlpatterns = [
    path('staff/', staff_dashboard_site.urls, name='staff'),
    path("", index, name="index")
]
