from django.urls import path
from . import dash_plotly
from . import dash_table
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reset', views.resetAll, name='reset_workspace'),
    path('upload', views.file_upload, name='upload'),
    path('loader', views.load_df, name="loader"),
    path('table', views.show_table, name='get_files'),
    path('exec/cleaner', views.cleaner, name="cleaner"),
    path('exec/joiner', views.joiner, name="joiner"),
    path('exec/viewer', views.viewer, name='viewer'),
    path('exec/exporter', views.exporter, name='exporter'),
    path('exec/transformer', views.transformer, name='transformer'),
    path('add/cleaner', views.addCleaner, name='addCleaner'),
    path('add/visualiser', views.addVisualizer, name='addVisualiser'),
    path('add/joiner', views.addJoiner, name='addJoiner'),
    path('add/viewer', views.addViewer, name='addViewer'),
    path('add/transformer', views.addTransformer, name='addTransformer'),
    path('add/exporter', views.addExporter, name="addExporter")
]