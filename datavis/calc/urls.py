from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.file_upload, name='upload'),
    path('cols', views.get_columns, name='get_cols'),
    path('table', views.show_table, name='get_files')
]