from django.urls import path

from . import views

urlpatterns = [
    # 만든 애플리케이션을 프로젝트에 삽입.
    path('', views.index, name='index'),
]