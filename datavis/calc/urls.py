from django.urls import path
from . import dash_plotly
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.file_upload, name='upload'),
    path('loader', views.load_df, name="loader"),
    path('cols', views.get_columns, name='get_cols'),
    path('table', views.show_table, name='get_files'),
    path('add/cleaner', views.addCleaner, name='addCleaner'),
    path('add/visualiser', views.addVisualizer, name='addVisualiser'),
    path('add/viewer', views.addViewer, name='addViewer'),
    path('add/transformer', views.addTransformer, name='addTransformer')
]