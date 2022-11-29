from django.urls import path
from .views import indexPageView, dashboardPageView, infoPageView, testPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("dashboard", dashboardPageView, name='dashboard'),
    path("info", infoPageView, name='info'),
    path("test", testPageView, name='test')
]