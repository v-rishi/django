from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('poll/<int:pk>',views.DetailView.as_view(), name='detail'),
    path('poll/<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('poll/<int:question_id>/vote/',views.vote,name='vote'),
]
