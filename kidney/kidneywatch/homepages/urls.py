from django.urls import path
from .views import indexPageView
from .views import dashboardPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("/dashboard", dashboardPageView, name='dashboard')
]