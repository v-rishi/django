from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name="index"),
    path('poll/<int:question_id>',views.detail, name='detail'),
    path('poll/<int:question_id>/results/',views.results,name='results'),
    path('poll/<int:question_id>/vote/',views.vote,name='vote'),
]
