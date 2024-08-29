from django.urls import path

from . import views
from h4site.views import IndexView, Index2View, SubView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexView.as_view(), name="index"),
    path('2', Index2View.as_view(), name="index2"),
    path('sub', SubView.as_view(), name="sub"),
]