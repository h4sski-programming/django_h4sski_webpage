from django.urls import path

from . import views
from h4site.views import IndexView, SubView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexView.as_view(), name="index"),
    path('sub', SubView.as_view(), name="sub"),
]